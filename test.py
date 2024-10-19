import requests
from encrypt.a_bogus import init_ctx
from encrypt.ms_token import get_ms_token

# a_bogus
js_context = init_ctx()


def register_alias():
    # 基础url
    base_url = "https://kol.fanqieopen.com/api/platform/promotion/plan/create/v:version"

    # 请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "cookie": "s_v_web_id=verify_m0wfjtcv_9tSjfTAx_v7G2_4q92_9Tyy_8RH3vrVBmxko; passport_csrf_token=68c5c396cea1fc02ab53e26fbd945dc8; passport_csrf_token_default=68c5c396cea1fc02ab53e26fbd945dc8; is_staff_user=false; store-region=cn-fj; store-region-src=uid; passport_mfa_token=CjjkVzH0p%2FC%2BPNJrvszddzG0Jv8%2BTyHcmoMPPD48DZi29BikheFHaFlvA2tTJxLnfGhF1NpKwi0h%2BhpKCjwpDxMTK45Q%2F7kwANqck6xyBBxpNRVr1%2FF0FuyklUlW8i5q8JZRqCKJuLrLPtsSBQCb5d3mIq4NteNdaYQQgvTbDRj2sdFsIAIiAQPsJMzK; d_ticket=992e4240ef72e4029be90c8ca30c78f9bef77; odin_tt=0e0cfc858954622db202fc78ddd3553a845ba8fbeb85a4bc4b52f6478d59b7e028f0b463d0ab8e28aabdf7527d50cf557baaf191855e8b1974b90e3fbbb42b9a; n_mh=k-YxOBUiIdQmBZedSNJszwtgnGm-hqrGuMKWJVnITeA; sid_guard=ace25384a88193f034dc6aa4a581da42%7C1726142422%7C5184000%7CMon%2C+11-Nov-2024+12%3A00%3A22+GMT; uid_tt=9dede313c7befd9b907cdc257c738b9a; uid_tt_ss=9dede313c7befd9b907cdc257c738b9a; sid_tt=ace25384a88193f034dc6aa4a581da42; sessionid=ace25384a88193f034dc6aa4a581da42; sessionid_ss=ace25384a88193f034dc6aa4a581da42; sid_ucp_v1=1.0.0-KGNlNDRmYzhhODVhOWU2NmQwN2ZmMjRkZGM4MzhmYmVmYzA4YWMzMGQKIAiksuDNzMzNAhDWr4u3Bhjj9xsgDDD_t7KyBjgCQPEHGgJobCIgYWNlMjUzODRhODgxOTNmMDM0ZGM2YWE0YTU4MWRhNDI; ssid_ucp_v1=1.0.0-KGNlNDRmYzhhODVhOWU2NmQwN2ZmMjRkZGM4MzhmYmVmYzA4YWMzMGQKIAiksuDNzMzNAhDWr4u3Bhjj9xsgDDD_t7KyBjgCQPEHGgJobCIgYWNlMjUzODRhODgxOTNmMDM0ZGM2YWE0YTU4MWRhNDI; ttwid=1%7CMG5RIzwcM10q19Krht6_TACKoHnnrNgYoimSVeGj2E0%7C1729322559%7Ccf9729414728327a5d59e664f77e3ca3f74f47ab1b196c588d0cad4496e1156f",
        "origin": "https://kol.fanqieopen.com",
        "priority": "u=1, i",
        "referer": "https://kol.fanqieopen.com/page/content?tab_type=2&top_tab_genre=-1",
        "sec-ch-ua": '"Google Chrome;v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
    }

    # 查询参数拼接到url
    params = {
        "appid": "457699",
        "aid": "457699",
        "origin_app_id": "457699",
        "host_app_id": "457699",
        "msToken": get_ms_token(160),
        "a_bogus": js_context.call(
            "generate_a_bogus",
            "device_platform=webapp&aid=6383&channel=channel_pc_web&publish_video_strategy_type=2&source=channel_pc_web&sec_user_id=MS4wLjABAAAAARbzTNzTdRkfL7E8-HKgy5_B7gWHrUpZFGPtj2vGJExStAYWRbnabJFbdVlbr98a&personal_center_strategy=1&update_version_code=170400&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=123.0.0.0&browser_online=true&engine_name=Blink&engine_version=123.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7362942367496504871",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        ),
    }

    print(params)

    # 请求体数据
    json_data = {
        "alias_name": "我在遥远的地方等你",
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

    resp = requests.post(base_url, headers=headers, params=params, json=json_data)

    print(resp.url, resp.status_code)


register_alias()
