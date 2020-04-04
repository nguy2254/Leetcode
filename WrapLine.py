class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        font_total = 0
        line_total = 1
        for character in S:
            width = widths[ord(character) - ord('a')]
            font_total = font_total + width
            if font_total > 100:
                line_total +=1
                font_total = width 
        return [line_total,font_total]
