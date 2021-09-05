class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        domains = {}
        for list_item in cpdomains:
            count, cpdomain = tuple(list_item.split(" "))
            count = int(count)
            split_domain = cpdomain.split(".")
            for index in range(len(split_domain)):
                domain = ".".join(split_domain[index:])
                if domain not in domains:
                    domains[domain] = 0
                domains[domain] += count
        return sorted([f"{c} {d}" for d, c in domains.items()])


examples: list[tuple[tuple[list[str]], list[str]]] = [
    (
        (["9001 discuss.leetcode.com"],),
        sorted(["9001 leetcode.com", "9001 discuss.leetcode.com", "9001 com"]),
    ),
    (
        (["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"],),
        sorted(
            [
                "901 mail.com",
                "50 yahoo.com",
                "900 google.mail.com",
                "5 wiki.org",
                "5 org",
                "1 intel.mail.com",
                "951 com",
            ]
        ),
    ),
]
