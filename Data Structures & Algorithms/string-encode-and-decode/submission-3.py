class Solution:

    def encode(self, strs: List[str]) -> str:
        return 'а'.join(strs) if len(strs) != 0 else 'э'

    def decode(self, s: str) -> List[str]:
        if s == 'э':
            return []
        return s.split('а') if len(s) != 0 else ['']
