import pyrato


def truncated_schroeder_integration(rir, limit=None):
    if limit is not None:
        idx = rir.find_nearest_time(limit)
        rir_copy = rir.copy()
        rir_copy.time[:, idx:] = 0.
    else:
        rir_copy = rir.copy()
    return pyrato.schroeder_integration(rir_copy, is_energy=False)
