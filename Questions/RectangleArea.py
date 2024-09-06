class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        first_rectangle = (ax2-ax1)*(ay2-ay1)
        second_rectangle = (bx2-bx1)*(by2-by1)
        overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))
        overlap_height = max(0, min(ay2, by2) - max(ay1, by1))
        
        # Area of the overlapping part
        overlap_area = overlap_width * overlap_height
        
        # Total area = Area1 + Area2 - Overlapping area
        total_area = first_rectangle + second_rectangle - overlap_area
        return total_area 
    