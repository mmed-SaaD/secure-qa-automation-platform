import http from 'k6/http';
import {check, sleep} from 'k6';
import {Trend, Rate} from 'k6/metrics';

import { BASE_URL, THINKING_TIME } from '../helpers/config.js';
import { buildGetParams } from '../helpers/requests.js';
import { commonJsonChecks, productsListChecks } from '../helpers/checks.js';

const productsDuration = new Trend('products_duration', true);
const productsContentValid = new Rate('products_content_valid');


export const options = {
  scenarios: {
    products_list_smoke: {
      executor: 'constant-vus',
      vus: 1,
      duration: '30s',
    },
  },
  thresholds: {
    http_req_failed: [{ threshold: 'rate==0', abortOnFail: true }],
    products_duration: [
      { threshold: 'p(95)<500', abortOnFail: true },
      { threshold: 'avg<300', abortOnFail: true },
    ],
    products_content_valid: [{ threshold: 'rate>0.99', abortOnFail: true }],
  },
};

const ENDPOINT = __ENV.ENDPOINT || "/products";

export default function () {
  const url = `${BASE_URL}${ENDPOINT}`;
  const params = buildGetParams('GET /products', 'list_products');

  const res = http.get(url, params);
  productsDuration.add(res.timings.duration);

  const isValid = check(res, {
    ...commonJsonChecks(),
    ...productsListChecks(),
  });

  productsContentValid.add(isValid);
  sleep(THINKING_TIME);
}