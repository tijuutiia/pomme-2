def distance_pt_pt(coords1, coords2):
    a, b, c =coords1
    d, e, f = coords2
    d= (d-a, e-b, f-c)
    return d