'''
Source:
Explaination: http://www.lucainvernizzi.net/blog/2014/11/21/codility-beta-challenge-number-of-disc-intersections/
Code: https://www.martinkysel.com/codility-number-of-disc-intersections-2010-beta-solution/
'''


def solution(A):
    circle_endpoints = []
    # True marks the beginning, False fo ending
    for i, a in enumerate(A):
        circle_endpoints += [(i-a, True), (i+a, False)]

    # sort the endpoints by two keys:
    # position of beginning, beginning should be ahead of ending
    circle_endpoints.sort(key=lambda x: (x[0], not x[1]))

    intersections, active_circles = 0, 0
    for _, is_beginning in circle_endpoints:
        if is_beginning:
            intersections += active_circles
            active_circles += 1
        else:
            active_circles -= 1
        if intersections > 10E6:
            return -1

    return intersections
