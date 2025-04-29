import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.colors as colors

TINY_SIZE = 4
SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=TINY_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=TINY_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

color_list = [
    "black", 
    "blue", 
    "red", 
    "green", 
    "yellow", 
    "gray", 
    "fuchsia", 
    "orange", 
    "teal", 
    "maroon"
]

st.set_page_config(layout="wide")
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)


st.title("Baby ARC Doo Doo Doo Doo Doo Doo Doo")

with st.sidebar:
    st.write("# Select")
    split = st.radio("Select a Split", ["training", "evaluation", "test"], horizontal=True)
    data_dpath = Path("data/")
    fpath = data_dpath / f"arc-agi_{split}_challenges.json"
    with open(fpath) as f:
        data = json.load(f)
    puzzle_ids = data.keys()
    puzzle_id = st.selectbox("Select a Puzzle ID", puzzle_ids)

    st.write("# Config")
    axis_on = st.radio("Show Axes", [True, False], horizontal=True)
    annotation_on = st.radio("Show Annotation", [True, False], horizontal=True)

st.write(f"## Puzzle `{puzzle_id}`")

st.write("## Train")
puzzle_split = "train"

def display_grid(grid: list, axis_on: bool, annotation_on: bool) -> None:
    fig, _ = plt.subplots(figsize=(3, 3))
    cmap = colors.ListedColormap(color_list)
    norm = colors.BoundaryNorm(list(range(len(color_list))), cmap.N)
    _ = plt.imshow(np.array(grid), cmap=cmap, norm=norm)
    
    # fig.tight_layout()

    fig = display_axes(fig, grid) if axis_on else remove_axes(fig)
    fig = annotate_grid(fig, grid) if annotation_on else fig
    
    st.pyplot(fig, use_container_width=False)

def display_axes(fig: plt.Figure, grid: list) -> plt.Figure:
    fig.axes[0].set_xticks(np.arange(len(grid[0])))
    fig.axes[0].set_yticks(np.arange(len(grid)))

    return fig

def remove_axes(fig: plt.Figure) -> plt.Figure:
    fig.axes[0].set_xticks([])
    fig.axes[0].set_yticks([])

    return fig

def annotate_grid(fig: plt.figure, grid: list) -> plt.figure:
    ax = fig.get_axes().pop()
    light_colors = [2, 4, 6, 7]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            val = grid[i][j]
            color = "white" if val not in light_colors else "black"
            ax.text(j, i, val, ha='center', va='center', color=color)
    return fig


# === Visuals
cols = st.columns(2)
cols[0].write("### Input")
cols[1].write("### Output")

for example in data[puzzle_id][puzzle_split]:
    cols = st.columns(2)
    with cols[0]:
        display_grid(example["input"], axis_on, annotation_on)
    with cols[1]:
        display_grid(example["output"], axis_on, annotation_on)

st.write("## Test")
puzzle_split = "test"
cols = st.columns(2)
with cols[0]:
    st.write("### Input")
    for example in data[puzzle_id][puzzle_split]:
        display_grid(example["input"], axis_on, annotation_on)
with cols[1]:
    st.write("### Output?")