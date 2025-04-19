from math import cos, sin


def is_point_in_semicircle(x, y, center_x, center_y, radius, angle):

    x_translated = x - center_x
    y_translated = y - center_y
    
    angle_rad = -angle * (3.14159265358979323846 / 180.0)
    x_rotated = x_translated * cos(angle_rad) - y_translated * sin(angle_rad)
    y_rotated = x_translated * sin(angle_rad) + y_translated * cos(angle_rad)
    
    dist_squared = x_rotated * x_rotated + y_rotated * y_rotated
    return dist_squared <= radius * radius and y_rotated >= 0

def line_intersects_semicircle(ax, ay, bx, by, center_x, center_y, radius, angle, eps=0.0101):
    def check_point(t):
        x = ax + (bx - ax) * t
        y = ay + (by - ay) * t
        return is_point_in_semicircle(x, y, center_x, center_y, radius, angle)
    
    if check_point(0) or check_point(1):
        return True
        
    left, right = 0, 1
    for _ in range(100):
        if right - left < eps:
            break
            
        mid = (left + right) / 2
        if check_point(mid):
            return True
            
        mid_left = (left + mid) / 2
        mid_right = (mid + right) / 2
        
        if check_point(mid_left):
            right = mid
        elif check_point(mid_right):
            left = mid
        else:
            left_inside = check_point(left)
            right_inside = check_point(right)
            if left_inside != check_point(mid):
                right = mid
            elif right_inside != check_point(mid):
                left = mid
            else:
                break
                
    return False

def main():
    from math import cos, sin
    
    n, x, y, r, t = map(int, input().split())
    
    for _ in range(n):
        ax, ay, bx, by = map(int, input().split())
        
        affected = line_intersects_semicircle(ax, ay, bx, by, x, y, r, t)
        print("Yes" if affected else "No")


main()