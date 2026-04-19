import http from 'k6/http';
import { check, sleep } from 'k6';

import { BASE_URL, THINKING_TIME } from '../helpers/config.js';
import { commonJsonChecks, searchProductByIdChecks} from '../helpers/checks.js';
import { buildGetParams } from '../helpers/requests.js';
import { buildSummary } from '../helpers/summary.js';

export const options = {
  scenarios: {
    search_product_soak: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '1m', target: 10 },
        { duration: '20m', target: 20 },
        { duration: '1m', target: 0 },
      ],
      gracefulRampDown: '10s',
    },
  },
  thresholds: {
    http_req_failed: [{ threshold: 'rate<0.01', abortOnFail: true }],
    http_req_duration: [
      { threshold: 'p(95)<800', abortOnFail: true },
      { threshold: 'avg<500', abortOnFail: true },
    ],
    checks: [{ threshold: 'rate>0.99', abortOnFail: true }],
  },
};

const ENDPOINT = __ENV.ENDPOINT || "/products";
const PRODUCT_ID = Number(__ENV.PRODUCT_ID) || 7;

export default function () {
  const url = `${BASE_URL}${ENDPOINT}/${PRODUCT_ID}`;
  const params = buildGetParams('GET /products/:id', 'get_product_by_id');

  const res = http.get(url, params);

  check(res, {
    ...commonJsonChecks(),
    ...searchProductByIdChecks(PRODUCT_ID)
  });
  sleep(THINKING_TIME);
}

export function handleSummary(data) {
  return buildSummary(data, 'k6 Soak Test Summary');
}