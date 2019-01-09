#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "tjhindman"

import cProfile
import pstats
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    def wrapper_func(*args, **kwargs):
        pr_obj = cProfile.Profile()

        pr_obj.enable()
        orig_res = func(*args, **kwargs)
        pr_obj.disable()

        s_obj = pstats.Stats(pr_obj)
        s_obj.sort_stats('cumulative')
        s_obj.print_stats()

        return orig_res

    return wrapper_func


def log_it(func):
    """Logging the entrance and exit of a function, mother fucker."""
    def wrapper_func(*args, **kwargs):
        print "Entering function: {}".format(func.__name__)
        res = func(*args, **kwargs)
        print "Leaving function: {}".format(func.__name__)
        return res

    return wrapper_func


def read_movies(src):
    """Read a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Case insensitive search within a list"""
    for movie in movies:
        if movie.lower() == title:
            return True
    return False


@profile
@log_it
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = []
    for movie in movies:
        if is_duplicate(movie.lower(), movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(stmt="find_duplicate_movies('movies.txt')",
                     setup="from __main__ import find_duplicate_movies")
    repeats = 7
    runs_per_rpt = 5
    res = t.repeat(repeat=repeats, number=runs_per_rpt)


    print "Best time across {} repeats of {} runs per repeat: {}".format(
        repeats, runs_per_rpt, min(res) / runs_per_rpt)


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))
    timeit_helper()


if __name__ == '__main__':
    main()
