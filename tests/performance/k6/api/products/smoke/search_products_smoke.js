import http from 'k6/http';
import {check, sleep} from 'k6';
import {Trend, Rate} from 'k6/metrics';

import { BASE_URL, THINKING_TIME } from '../helpers/config.js';
import { buildGetParams } from '../helpers/requests.js';
import { commonJsonChecks, searchProductChecks } from '../helpers/checks.js';

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
      { threshold: 'p(95)<600', abortOnFail: true },
      { threshold: 'avg<400', abortOnFail: true },
    ],
    products_content_valid: [{ threshold: 'rate>0.99', abortOnFail: true }],
  },
};

const ENDPOINT = __ENV.ENDPOINT || "/products/search";
const KEYWORD = __ENV.KEYWORD || "laptop";

export default function () {
  const url = `${BASE_URL}${ENDPOINT}?q=${KEYWORD}`;
  const params = buildGetParams('GET /products/search', 'search_product');

  const res = http.get(url, params);
  productsDuration.add(res.timings.duration);

  const isValid = check(res, {
    ...commonJsonChecks(),
    ...searchProductChecks(KEYWORD)
  });

  productsContentValid.add(isValid);
  sleep(THINKING_TIME);
}