from random import randint

import perfplot

from sorting import (
    bubble_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    tim_sort,
    python_built_in_sort,
)


perfplot.show(
    n_range=range(0, 1000, 100),
    setup=lambda n: [randint(0, 1000) for _ in range(n)],
    kernels=[
        bubble_sort,
        insertion_sort,
        merge_sort,
        quick_sort,
        tim_sort,
        python_built_in_sort,
    ],
)