import yaml
import re

def load_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def save_yaml(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        yaml.safe_dump(data, file, allow_unicode=True)

def extract_country(proxy_name):
    country_patterns = {
        '香港': re.compile(r'香港|HK', re.IGNORECASE),
        '新加坡': re.compile(r'新加坡', re.IGNORECASE),
        '日本': re.compile(r'日本', re.IGNORECASE),
        '台湾': re.compile(r'台湾|TW', re.IGNORECASE),
        '美国': re.compile(r'美国|US', re.IGNORECASE),
        '韩国': re.compile(r'韩国', re.IGNORECASE),
        '泰国': re.compile(r'泰国', re.IGNORECASE),
        '加拿大': re.compile(r'加拿大', re.IGNORECASE),
        '法国': re.compile(r'法国', re.IGNORECASE),
        '英国': re.compile(r'英国', re.IGNORECASE),
        '印度': re.compile(r'印度', re.IGNORECASE),
        '德国': re.compile(r'德国', re.IGNORECASE),
        '西班牙': re.compile(r'西班牙', re.IGNORECASE),
        '澳大利亚': re.compile(r'澳大利亚', re.IGNORECASE),
        '阿联酋': re.compile(r'阿联酋', re.IGNORECASE),
        '巴基斯坦': re.compile(r'巴基斯坦', re.IGNORECASE),
        '马来西亚': re.compile(r'马来西亚', re.IGNORECASE),
        '印度尼西亚': re.compile(r'印度尼西亚', re.IGNORECASE),
        '尼日利亚': re.compile(r'尼日利亚', re.IGNORECASE),
        '荷兰': re.compile(r'荷兰', re.IGNORECASE),
        '朝鲜': re.compile(r'朝鲜', re.IGNORECASE),
        '越南': re.compile(r'越南', re.IGNORECASE),
        '孟加拉': re.compile(r'孟加拉', re.IGNORECASE),
        # 其他国家可以在这里继续添加
    }

    for country, pattern in country_patterns.items():
        if pattern.search(proxy_name):
            return country
    return '其他'

def group_proxies_by_country(proxies):
    grouped_proxies = {
        '香港': [],
        '新加坡': [],
        '日本': [],
        '台湾': [],
        '美国': [],
        '韩国': [],
        '泰国': [],
        '加拿大': [],
        '法国': [],
        '英国': [],
        '印度': [],
        '德国': [],
        '西班牙': [],
        '澳大利亚': [],
        '阿联酋': [],
        '巴基斯坦': [],
        '马来西亚': [],
        '印度尼西亚': [],
        '尼日利亚': [],
        '荷兰': [],
        '朝鲜': [],
        '越南': [],
        '孟加拉': [],
    }
    for proxy in proxies:
        country = extract_country(proxy['name'])
        if country not in grouped_proxies:
            grouped_proxies[country] = []
        grouped_proxies[country].append(proxy)
    return grouped_proxies

def create_proxy_groups(grouped_proxies):
    proxy_groups = []
    for country, proxies in grouped_proxies.items():
        if(len(proxies) > 0) :
            group = {
                'name': f'{country} Group',
                'type': 'select',
                'proxies': [proxy['name'] for proxy in proxies]
            }
            proxy_groups.append(group)
    return proxy_groups

def main():
    # 读取原始代理配置文件
    proxies_data = load_yaml('data/proxies.yaml')

    # 按国家分组代理
    grouped_proxies = group_proxies_by_country(proxies_data['proxies'])

    # 创建proxy-groups
    proxy_groups = create_proxy_groups(grouped_proxies)


    # 写入新文件
    proxy_config = load_yaml('data/proxy-config.yaml')

    proxy_config["proxies"] = proxies_data['proxies']
    proxy_config["proxy-groups"] = proxy_groups

    save_yaml(proxy_config, 'data/proxy-config.yaml')

if __name__ == '__main__':
    main()
