import http from 'k6/http';
import { check, sleep, fail } from 'k6';
import { Trend, Rate } from 'k6/metrics';

import { BASE_URL, THINKING_TIME } from '../helpers/config.js';
import { buildGetParams } from '../helpers/requests.js';
import { buildSummary } from '../helpers/summary.js';
import { authUserChecks, commonJsonChecks, loginChecks, productsListChecks } from '../helpers/checks.js';

const productsDuration = new Trend('products_duration', true);
const productsContentValid = new Rate('products_content_valid');

export const options = {
  scenarios: {
    e2e_workflow_load: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '1m', target: 5 },
        { duration: '1m', target: 10 },
        { duration: '10m', target: 15 },
        { duration: '1m', target: 0 },
      ],
      gracefulRampDown: '10s',
    },
  },
  thresholds: {
    http_req_failed: [{ threshold: 'rate<0.01', abortOnFail: true }],
    'http_req_duration{expected_response:true}': [
      { threshold: 'p(95)<2200', abortOnFail: true },
      { threshold: 'avg<1400', abortOnFail: true },
    ],
    checks: [{ threshold: 'rate>0.99', abortOnFail: true }],
  },
};

const AUTH_ENDPOINT = __ENV.AUTH_ENDPOINT || '/auth/login';
const GET_AUTH_USER_ENDPOINT = __ENV.GET_AUTH_USER_ENDPOINT || '/auth/me';
const GET_AUTH_PRODUCTS = __ENV.GET_AUTH_PRODUCTS || '/auth/products';
const USERNAME = __ENV.USERNAME || 'jamesd';
const PASSWORD = __ENV.PASSWORD || 'jamesdpass';

export default function () {
  let url = `${BASE_URL}${AUTH_ENDPOINT}`;
  let params = {
    headers: {
      'Content-Type': 'application/json',
    },
    ...buildGetParams('POST /auth/login', 'login_user'),
  };

  const loginCredentials = JSON.stringify({
    username: USERNAME,
    password: PASSWORD,
  });

  let res = http.post(url, loginCredentials, params);

  const loginOk = check(res, {
    ...commonJsonChecks(),
    ...loginChecks(4),
    'login returned accessToken': (r) => !!r.json('accessToken'),
  });

  if (!loginOk) {
    console.error(`LOGIN FAILED | status=${res.status} | body=${res.body}`);
    fail(`Stopping iteration ... login failed with status ${res.status}`);
  }

  const accessToken = res.json('accessToken');

  url = `${BASE_URL}${GET_AUTH_USER_ENDPOINT}`;
  params = {
    ...buildGetParams('GET /auth/me', 'get_logged_user_info'),
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${accessToken}`,
    },
  };

  res = http.get(url, params);

  const authUserOk = check(res, {
    ...commonJsonChecks(),
    ...authUserChecks(4),
  });

  if (!authUserOk) {
    console.error(`/auth/me FAILED | status=${res.status} | body=${res.body}`);
  }

  url = `${BASE_URL}${GET_AUTH_PRODUCTS}`;
  params = {
    ...buildGetParams('GET /auth/products', 'get_products_as_authorized_user'),
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${accessToken}`,
    },
  };

  res = http.get(url, params);

  const productsOk = check(res, {
    ...commonJsonChecks(),
    ...productsListChecks(),
  });

  if (!productsOk) {
    console.error(`/auth/products FAILED | status=${res.status} | body=${res.body}`);
  }

  sleep(THINKING_TIME);
}

export function handleSummary(data) {
  return buildSummary(data, 'k6 Load Test Summary');
}