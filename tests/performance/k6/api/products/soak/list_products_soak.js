import http from 'k6/http';
import {check, sleep} from 'k6';

import { commonJsonChecks, productsListChecks } from '../helpers/checks.js';
import { buildGetParams } from '../helpers/requests.js';
import { BASE_URL, THINKING_TIME } from '../helpers/config.js';

export const options = {
    scenarios : {
        products_list : {
            executor : 'ramping-vus',
            startVUs : 0,
            stages : [
                {duration : '1m', target : 10},
                {duration : '1m', target : 20},
                {duration : '10m', target : 30},
                {duration : '1m', target : 0},
            ],
            gracefulRampDown : '10s',
        },
    },
    thresholds : {
        http_req_failed : [
            {threshold : 'rate==0', abortOnFail : true},
        ],
        http_req_duration : [
            {threshold : 'p(95)<500', abortOnFail : true},
            {threshold : 'avg<300', abortOnFail : true}
        ],
        checks : [
            {threshold : 'rate==1', abortOnFail: true}
        ],
    },
};

const ENDPOINT = __ENV.ENDPOINT || "/products";

export default function(){
    const url = `${BASE_URL}${ENDPOINT}`;
    const params = buildGetParams('GET /products', 'list_products');
    const res = http.get(url, params);

    check(res, {
        ...commonJsonChecks(),
        ...productsListChecks()
    });
    
    sleep(THINKING_TIME)
}
