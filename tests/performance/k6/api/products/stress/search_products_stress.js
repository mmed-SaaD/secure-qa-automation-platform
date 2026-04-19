import http from 'k6/http';
import {check, sleep} from 'k6';

import { commonJsonChecks, searchProductChecks } from '../helpers/checks.js';
import { BASE_URL, THINKING_TIME } from '../helpers/config.js';
import { buildGetParams } from '../helpers/requests.js';

export const options = {
    scenarios : {
        search_product : {
            executor : 'ramping-vus',
            startVUs : 0,
            stages : [
                {duration : '30s', target : 10},
                {duration : '30s', target : 20},
                {duration : '30s', target : 40},
                {duration : '30s', target : 80},
                {duration : '30s', target : 0},
            ],
            gracefulRampDown : '10s',
        },
    },
    thresholds : {
        http_req_failed : [
            {threshold : 'rate<0.01'},
        ],
        http_req_duration : [
            {threshold : 'p(95)<1200'},
            {threshold : 'avg<800'},
        ],
        checks : [
            {threshold : 'rate>0.99'}
        ],
    },
};

const ENDPOINT = __ENV.ENDPOINT || "/products/search";
const KEYWORD = __ENV.KEYWORD || "phone";


export default function(){
    const url = `${BASE_URL}${ENDPOINT}?q=${KEYWORD}`;
    const params = buildGetParams('GET /products/search', 'search_product');
    const res = http.get(url, params);

    check(res, {
        ...commonJsonChecks(),
        ...searchProductChecks(KEYWORD)
    });
    sleep(THINKING_TIME);
}
