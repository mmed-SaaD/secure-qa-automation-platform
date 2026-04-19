import http from 'k6/http';
import {check, sleep} from 'k6';
import {Trend, Rate} from 'k6/metrics';

import { BASE_URL, THINKING_TIME } from '../helpers/config.js';
import { buildGetParams } from '../helpers/requests.js';
import { authUserChecks, commonJsonChecks, loginChecks, productsListChecks } from '../helpers/checks.js';

const productsDuration = new Trend('products_duration', true);
const productsContentValid = new Rate('products_content_valid');

export const options = {
  scenarios: {
    search_product_load: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '1m', target: 5 },
        { duration: '1m', target: 10 },
        { duration: '1m', target: 15 },
        { duration: '1m', target: 0 },
      ],
      gracefulRampDown: '10s',
    },
  },
  thresholds: {
    http_req_failed: [{ threshold: 'rate<0.01', abortOnFail: true }],
    http_req_duration: [
      { threshold: 'p(95)<2000', abortOnFail: true },
      { threshold: 'p(90)<1600', abortOnFail: true },
      { threshold: 'avg<1200', abortOnFail: true },
    ],
    checks: [{ threshold: 'rate>0.99', abortOnFail: true }],
  },
};

const AUTH_ENDPOINT = __ENV.AUTH_ENDPOINT || "/auth/login";
const GET_AUTH_USER_ENDPOINT = __ENV.GET_AUTH_USER_ENDPOINT || "/auth/me";
const GET_AUTH_PRODUCTS = __ENV.GET_AUTH_PRODUCTS || "/auth/products";
const USERNAME = __ENV.USERNAME || "jamesd";
const PASSWORD = __ENV.PASSWORD || "jamesdpass";

export default function(){
    var url = `${BASE_URL}${AUTH_ENDPOINT}`;
    var params = {
       headers : {
        'Content-Type' : 'application/json',
       },
       ...buildGetParams('POST /auth/login', 'login_user'),  
    }
    const login_credentials = JSON.stringify({
        'username' : USERNAME,
        'password' : PASSWORD,
    });
    var res = http.post(url, login_credentials, params);
    const accessToken = res.json("accessToken");
    check(res, {
        ...commonJsonChecks(),
        ...loginChecks(4),
    });

    url = `${BASE_URL}${GET_AUTH_USER_ENDPOINT}`;
    params = {
        ...buildGetParams('GET /auth/me', 'get_logged_user_info'),
        headers : {
            'Content-Type' : 'application/json',
            'Authorization' : `Bearer ${accessToken}`
        },
    }
    res = http.get(url, params);
    check(res, {
        ...commonJsonChecks(),
        ...authUserChecks(4),
    });
    
    url = `${BASE_URL}${GET_AUTH_PRODUCTS}`;
    params = {
        ...buildGetParams('GET /auth/products', 'get_products_as_authorized_user'),
        headers : {
            'Content-Type' : 'application/json',
            'Authorization' : `Bearer ${accessToken}`
        },
    }
    res = http.get(url, params);
    check(res, {
        ...commonJsonChecks(),
        ...productsListChecks(),
    });
    sleep(THINKING_TIME);
}

export function handleSummary(data) {
  return buildSummary(data, 'k6 Load Test Summary');
}