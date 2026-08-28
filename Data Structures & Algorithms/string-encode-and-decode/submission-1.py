class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "__EMPTY__"  # marker for empty list
        return '|'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "__EMPTY__":
            return []
        return s.split('|')
