import monotonic as mono
import time

EPS_C = 0.01

def test_monotonic():
    result = 0
    result_2 = 0
    for _ in range (100):
        self_mono_1 = mono.monotonic()
        self_mono_2 = mono.monotonic()
        result += self_mono_2 - self_mono_1

        mono_1 = time.monotonic()
        mono_2 = time.monotonic()
        result_2 += mono_2 - mono_1
    assert abs(result_2 - result) < EPS_C
