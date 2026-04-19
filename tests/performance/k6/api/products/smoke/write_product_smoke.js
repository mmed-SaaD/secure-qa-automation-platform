import http from 'k6/http';
import {check, sleep} from 'k6';
import {Trend, Rate} from 'k6/metrics';

import { BASE_URL, THINKING_TIME } from '../helpers/config.js';
import { buildGetParams } from '../helpers/requests.js';
import { assertProductAdded, commonJsonChecks } from '../helpers/checks.js';

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
      { threshold: 'p(95)<700', abortOnFail: true },
      { threshold: 'avg<500', abortOnFail: true },
    ],
    products_content_valid: [{ threshold: 'rate>0.99', abortOnFail: true }],
  },
};

const ENDPOINT = __ENV.ENDPOINT || "/products/add";

export default function () {
  const url = `${BASE_URL}${ENDPOINT}`;
  const params = buildGetParams('POST /products/add', 'add_product');
  const payload = JSON.stringify({
    "title": "Dior Sauvage Eau De Parfum",
    "description": "Sauvage by Dior is a bold and fresh fragrance with notes of bergamot, Sichuan pepper, and ambroxan. Ideal for both day and night wear.",
    "category": "fragrances",
    "price": 119.99,
    "discountPercentage": 12.75,
    "rating": 4.45,
    "stock": 72,
    "tags": ["fragrances", "perfumes"],
    "brand": "Dior",
    "sku": "FRA-DIO-SAU-001",
    "weight": 6,
    "dimensions": {
        "width": 22.1,
        "height": 24.3,
        "depth": 23.5
    },
    "warrantyInformation": "2 year warranty",
    "shippingInformation": "Ships within 2 days",
    "availabilityStatus": "In Stock",
    "reviews": [
        {
        "rating": 5,
        "comment": "Amazing scent, lasts all day!",
        "date": "2025-04-28T10:15:22.000Z",
        "reviewerName": "Omar Benali",
        "reviewerEmail": "omar.benali@x.dummyjson.com"
        },
        {
        "rating": 4,
        "comment": "Very good but a bit strong at first.",
        "date": "2025-04-29T14:22:10.000Z",
        "reviewerName": "Sara El Amrani",
        "reviewerEmail": "sara.elamrani@x.dummyjson.com"
        }
    ],
    "returnPolicy": "14 days return policy",
    "minimumOrderQuantity": 1,
    "meta": {
        "createdAt": "2025-04-28T10:15:22.000Z",
        "updatedAt": "2025-04-29T14:22:10.000Z",
        "barcode": "9876543210123",
        "qrCode": "https://cdn.dummyjson.com/public/qr-code.png"
    },
    "images": [
        "https://cdn.dummyjson.com/product-images/fragrances/dior-sauvage/1.webp",
        "https://cdn.dummyjson.com/product-images/fragrances/dior-sauvage/2.webp"
    ],
    "thumbnail": "https://cdn.dummyjson.com/product-images/fragrances/dior-sauvage/thumbnail.webp"
  });

  const res = http.post(url, payload, params);
  productsDuration.add(res.timings.duration);

  const isValid = check(res, {
    ...commonJsonChecks(),
    ...assertProductAdded()
  });

  productsContentValid.add(isValid);
  sleep(THINKING_TIME);
}