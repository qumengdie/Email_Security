"""
check if the given domain employed with DMARC, DKIM, SPF authentication protocal
"""

import dns.resolver


def check_DMARC(domain):
    # Testing DMARC
    try:
        test_dmarc = dns.resolver.resolve('_dmarc.' + domain, 'TXT')
        for dns_data in test_dmarc:
            if 'DMARC1' in str(dns_data):
                # print("  [PASS] DMARC record found :", dns_data)
                return True
    except:
        pass
        # print("  [FAIL] DMARC record not found.")

    return False


def check_DKIM(domain, selector):
    # Testing DKIM
    for i in range(0, len(selector)):
        try:
            test_dkim = dns.resolver.resolve(selector[i] + '._domainkey.' + domain, 'TXT')
            for dns_data in test_dkim:
                if 'DKIM1' in str(dns_data) or "k=rsa" in str(dns_data):
                    # print("  [PASS] DKIM record found  :", dns_data)
                    return True
        except:
            pass
            # print("  [FAIL] DKIM record not found.")

    return False


def check_SPF(domain):
    # Testing SPF
    try:
        test_spf = dns.resolver.resolve(domain, 'TXT')
        for dns_data in test_spf:
            if 'spf1' in str(dns_data):
                # print("  [PASS] SPF record found   :", dns_data)
                return True
    except:
        pass
        # print("  [FAIL] SPF record not found.")
    return False

def get_mx_record(domain):
    mx = []
    try:
        test_mx = dns.resolver.resolve(domain, 'MX')
        for mxdata in test_mx:
            # print(' MX Record:', mxdata.to_text())
            mx.append(mxdata)
            return mx
    except:
        pass
        # print("  [FAIL] MX record not found.")
    return []


def check_dds(domain):
    """_summary_
    Args:
        domain (str): nyu.edu
        selector (str, optional): _description_. Defaults to "mail".
    Returns:
        _type_: [False, False, False]
    """
    mx = get_mx_record(domain)
    spf = check_SPF(domain)
    selector = ['google', 'dkim', 'mail', 'default', 'selector', 'selector1', 'k1']
    dkim = check_DKIM(domain, selector)
    dmarc = check_DMARC(domain)
    return [mx, spf, dkim, dmarc]


if __name__ == "__main__":
    nyu = "nyu.edu"
    usas = "mails.ucas.ac.cn"
    nyulist = check_dds(nyu)
    usaslist = check_dds(usas)
    mitlist = check_dds("mit.edu")
    print(nyulist)
    print(usaslist)
    print(mitlist)
