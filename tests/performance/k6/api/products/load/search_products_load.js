import http from 'k6/http';
import { check, sleep } from 'k6';

import { BASE_URL, THINKING_TIME } from '../helpers/config.js';
import { commonJsonChecks, productsListChecks, searchProductChecks } from '../helpers/checks.js';
import { buildGetParams } from '../helpers/requests.js';
import { buildSummary } from '../helpers/summary.js';

const ENDPOINT = __ENV.ENDPOINT || "/products/search";
const KEYWORD = __ENV.KEYWORD || "phone";

export const options = {
  scenarios: {
    search_product_load: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '1m', target: 10 },
        { duration: '1m', target: 20 },
        { duration: '1m', target: 30 },
        { duration: '1m', target: 0 },
      ],
      gracefulRampDown: '10s',
    },
  },
  thresholds: {
    http_req_failed: [{ threshold: 'rate<0.01', abortOnFail: true }],
    http_req_duration: [
      { threshold: 'p(95)<900', abortOnFail: true },
      { threshold: 'p(90)<700', abortOnFail: true },
      { threshold: 'avg<500', abortOnFail: true },
    ],
    checks: [{ threshold: 'rate>0.99', abortOnFail: true }],
  },
};

export default function () {
  const url = `${BASE_URL}${ENDPOINT}?q=${KEYWORD}`;
  const params = buildGetParams('GET /products/search', 'search_product');

  const res = http.get(url, params);

  check(res, {
    ...commonJsonChecks(),
    ...searchProductChecks(KEYWORD)
  });

  sleep(THINKING_TIME);
}

export function handleSummary(data) {
  return buildSummary(data, 'k6 Load Test Summary');
}