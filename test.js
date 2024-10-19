
function register_alias() {
    const base_url = "https://kol.fanqieopen.com/api/platform/promotion/plan/create/v:version"

    const headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "cookie": "s_v_web_id=verify_m0wfjtcv_9tSjfTAx_v7G2_4q92_9Tyy_8RH3vrVBmxko; passport_csrf_token=68c5c396cea1fc02ab53e26fbd945dc8; passport_csrf_token_default=68c5c396cea1fc02ab53e26fbd945dc8; is_staff_user=false; store-region=cn-fj; store-region-src=uid; passport_mfa_token=CjjkVzH0p%2FC%2BPNJrvszddzG0Jv8%2BTyHcmoMPPD48DZi29BikheFHaFlvA2tTJxLnfGhF1NpKwi0h%2BhpKCjwpDxMTK45Q%2F7kwANqck6xyBBxpNRVr1%2FF0FuyklUlW8i5q8JZRqCKJuLrLPtsSBQCb5d3mIq4NteNdaYQQgvTbDRj2sdFsIAIiAQPsJMzK; d_ticket=992e4240ef72e4029be90c8ca30c78f9bef77; odin_tt=0e0cfc858954622db202fc78ddd3553a845ba8fbeb85a4bc4b52f6478d59b7e028f0b463d0ab8e28aabdf7527d50cf557baaf191855e8b1974b90e3fbbb42b9a; n_mh=k-YxOBUiIdQmBZedSNJszwtgnGm-hqrGuMKWJVnITeA; sid_guard=ace25384a88193f034dc6aa4a581da42%7C1726142422%7C5184000%7CMon%2C+11-Nov-2024+12%3A00%3A22+GMT; uid_tt=9dede313c7befd9b907cdc257c738b9a; uid_tt_ss=9dede313c7befd9b907cdc257c738b9a; sid_tt=ace25384a88193f034dc6aa4a581da42; sessionid=ace25384a88193f034dc6aa4a581da42; sessionid_ss=ace25384a88193f034dc6aa4a581da42; sid_ucp_v1=1.0.0-KGNlNDRmYzhhODVhOWU2NmQwN2ZmMjRkZGM4MzhmYmVmYzA4YWMzMGQKIAiksuDNzMzNAhDWr4u3Bhjj9xsgDDD_t7KyBjgCQPEHGgJobCIgYWNlMjUzODRhODgxOTNmMDM0ZGM2YWE0YTU4MWRhNDI; ssid_ucp_v1=1.0.0-KGNlNDRmYzhhODVhOWU2NmQwN2ZmMjRkZGM4MzhmYmVmYzA4YWMzMGQKIAiksuDNzMzNAhDWr4u3Bhjj9xsgDDD_t7KyBjgCQPEHGgJobCIgYWNlMjUzODRhODgxOTNmMDM0ZGM2YWE0YTU4MWRhNDI; ttwid=1%7CMG5RIzwcM10q19Krht6_TACKoHnnrNgYoimSVeGj2E0%7C1728784514%7Cb1c4589cafa484ee5dd2fd350ddd6082b9c7e8aac2e320ec3bcf0846b231c1b6",
    }

    const params = {
        "appid": "457699",
        "aid": "457699",
        "origin_app_id": "457699",
        "host_app_id": "457699",
        "msToken": "od5lK3ALQdIW3OXHOllbeFAC5YAM325SZktUtrMKYkDR77iay2mC6nO8h56R9BS296kBBw1YedlCb6bOOrk8KW-vbRZ8aHD5ak48UKLuAsXlIdX6gh81Rh-RyB3Y-9Q-O3AW7M8JxGjw4JyJ_F3X1Gb61cWHnpIi",
        "a_bogus": "xjWZBf8kdEIsvfj55fALfY3quo-oYmaK0cyeMD2WTQiSw639HMT59exEh8411U6jNT%2FdIeWjyThbYrngrQAr8ryUHWkoUdQ2m6gDKAFD-dSC5Ni7C6hgnz4wmkJlte525k1AE%2FiMq7%2FrSYuDloqe-XO4OgZCcNvhwyG7GIQCXfR3E-6%2FdOIVvj%3D%3D",
    }

    const json_data = {
        "alias_name": "你好我是你等",
        "alias_type": 1,
        "book_id": "7405440286622485566",
        "metrics_data": {
            "app_id": "457699",
            "app_name": "fanqie_novel",
            "create_entrance": "book_list",
            "genre": "203",
            "is_recommend": "1",
            "sub_page_name": "爆款榜",
        },
    }

    const url = `${base_url}?${new URLSearchParams(params).toString()}`

    fetch(url, {
        method: "POST",
        body: JSON.stringify(json_data),
        headers: headers
    }).then(resp => {
        console.log(resp);
        return resp.json()
    }).then(data => {
        console.log(data);
    })
}

register_alias()
