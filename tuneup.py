#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "Mike Boring"


import pstats
import functools
import timeit
import cProfile
import pstats
from pstats import SortKey
from collections import Counter


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    @functools.wraps(func)
    def wrapper_profile(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        func(*args, **kwargs)
        pr.disable()
        sortby = SortKey.CUMULATIVE
        ps = pstats.Stats(pr).strip_dirs().sort_stats(sortby)
        ps.print_stats()
        return func(*args, **kwargs)
    return wrapper_profile


def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


# def is_duplicate(title, movies):
#     """Returns True if title is within movies list."""
#     for movie in movies:
#         if movie.lower() == title.lower():
#             return True
#     return False


# @profile
# def find_duplicate_movies(src):
#     """Returns a list of duplicate movies from a src list."""
#     movies = read_movies(src)
#     duplicates = []
#     while movies:
#         movie = movies.pop()
#         if is_duplicate_improved2(movie, movies):
#             duplicates.append(movie)
#     return duplicates


@profile
def find_duplicate_movies_improved(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    c = Counter(movies)
    duplicates = []
    for movie in c:
        if c.get(movie) > 1:
            duplicates.append(movie)
    return duplicates


def timeit_helper(src):
    """Part A: Obtain some profiling measurements using timeit."""
    t = timeit.Timer(src)
    result = t.repeat(repeat=5, number=3)
    average_result = min(result)
    print(
        f'Best time across 5 repeats of 3 runs per repeat: {average_result} sec')
    return result


# @timeit_helper
def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies_improved('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))


# if __name__ == '__timeit_helper__':
if __name__ == '__main__':
    main()
