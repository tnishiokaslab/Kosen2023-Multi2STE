from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import numpy  as np
import pandas as pd

def fig_data1_and_2(fig1,fig2):
    fig = go.Figure(
        data=[fig1.data[0],fig1.data[1],fig1.data[2],fig1.data[3], 
              fig2.data[0],fig2.data[1],fig2.data[2],fig2.data[3],],
        layout=go.Layout(
            xaxis=dict(domain=[0, 0.5]),
            yaxis=dict(domain=[0, 1]),
            xaxis2=dict(domain=[0.5, 1]),
            yaxis2=dict(domain=[0, 1], anchor='x2'),
        )
    )
    
    #環境の設定
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=10),#余白left ,right ,bottom,top
                        font_size=10, hoverlabel_font_size=15,
                        width  = 800,
                        height = 550,
                        legend=dict(x=0.01,
                              y=0.99,
                              xanchor='left',
                              yanchor='top',
                              orientation='h',
                              ),
                        scene = dict(##シーン固定
                            xaxis = dict(range=[-1,1],),
                            yaxis = dict(range=[-1,1],),
                            zaxis = dict(range=[-1,1],),
                            xaxis_type="linear", yaxis_type="linear", zaxis_type="linear",
                            xaxis_dtick = 0.5, yaxis_dtick = 0.5, zaxis_dtick = 0.5,
                            aspectmode = "cube",
                            ),
                        scene_camera = dict(#カメラ設定
                                up=dict(x=0, y=0, z=1),
                                center=dict(x=0, y=0, z=0),
                                eye=dict(x=0.9, y=0.9, z=0.9)
                            )
                        )
    return fig

def fig_data_human36M(out_txt ,slider_value ,color_set1 ,width_set1 ,opacity_set1):
    fig = go.Figure()
    df1 = pd.DataFrame(out_txt,
                        columns=['x','z','y'])
    #マーカー1
    df_plot = df1[(slider_value*17-17):(slider_value*17)]
    fig.add_trace(
        go.Scatter3d(
            x = df_plot['x'],
            y = df_plot['y'],
            z = df_plot['z'],
            mode = 'markers',
            hoverinfo = "x+y+z",
            name = 'pose_point',
            marker=dict(
                color = color_set1,
                size = 3,
                opacity = 0.6,
            ),
        ) 
    )
    #線lines1
    df_plot = df1[(slider_value*17-17):(slider_value*17-13)]
    fig.add_trace(
        go.Scatter3d(
            x = df_plot['x'],
            y = df_plot['y'],
            z = df_plot['z'],
            mode = 'lines',
            #label='groupclick', 
            opacity = opacity_set1,
            legendgroup = 1,
            hoverinfo = "none",
            name = 'pose_bone',
            line = dict(
                color = color_set1,
                width = width_set1,
                ),    
        ) 
    )
    df_plot = df1.iloc[[(slider_value*17-7),(slider_value*17-8),(slider_value*17-9),(slider_value*17-10),(slider_value*17-17),(slider_value*17-13),(slider_value*17-12),(slider_value*17-11)]]
    fig.add_trace(
        go.Scatter3d(
            x = df_plot['x'],
            y = df_plot['y'],
            z = df_plot['z'],
            mode = 'lines',
            opacity = opacity_set1,
            legendgroup = 1,
            hoverinfo ="none",
            showlegend = False,
            line = dict(
                color = color_set1,
                width = width_set1,
                ),    
        ) 
    )
    df_plot = df1.iloc[[(slider_value*17-4),(slider_value*17-5),(slider_value*17-6),(slider_value*17-9),(slider_value*17-3),(slider_value*17-2),(slider_value*17-1)]]
    fig.add_trace(
        go.Scatter3d(
            x = df_plot['x'],
            y = df_plot['y'],
            z = df_plot['z'],
            mode = 'lines',
            opacity = opacity_set1,
            legendgroup = 1,
            hoverinfo ="none",
            showlegend = False,
            line = dict(
                color = color_set1,
                width = width_set1,
                ),    
        ) 
    )
    
    #環境の設定
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=10),#余白left ,right ,bottom,top
                        font_size=10, hoverlabel_font_size=15,
                        width  = 500,
                        height = 500,
                        legend=dict(x=0.01,
                              y=0.99,
                              xanchor='left',
                              yanchor='top',
                              orientation='h',
                              ),
                        scene = dict(##シーン固定
                            xaxis = dict(range=[-1,1],),
                            yaxis = dict(range=[-1,1],),
                            zaxis = dict(range=[-1,1],),
                            xaxis_type="linear", yaxis_type="linear", zaxis_type="linear",
                            xaxis_dtick = 0.5, yaxis_dtick = 0.5, zaxis_dtick = 0.5,
                            aspectmode = "cube",
                            ),
                        scene_camera = dict(#カメラ設定
                                up=dict(x=0, y=0, z=1),
                                center=dict(x=0, y=0, z=0),
                                eye=dict(x=0.9, y=0.9, z=0.9)
                            )
                        )
    return fig


def fig_data_panapotic(out_txt ,slider_value ,color_set1 ,width_set1 ,opacity_set1):
    fig = go.Figure()
    df1 = pd.DataFrame(out_txt,
                        columns=['x','z','y'])
    #マーカー1
    df_plot = df1[(slider_value*19-19):(slider_value*19-4)]
    fig.add_trace(
        go.Scatter3d(
            x = df_plot['x'],
            y = df_plot['y'],
            z = df_plot['z'],
            mode = 'markers',
            hoverinfo = "x+y+z",
            name = 'pose_point',
            marker=dict(
                color = color_set1,
                size = 3,
                opacity = 0.6,
            ),
        ) 
    )
    
    #線lines1
    df_plot = df1.iloc[[(slider_value*19-8),(slider_value*19-9),(slider_value*19-10),(slider_value*19-19),(slider_value*19-16),(slider_value*19-15),(slider_value*19-14)]]
    fig.add_trace(
        go.Scatter3d(
            x = df_plot['x'],
            y = df_plot['y'],
            z = df_plot['z'],
            mode = 'lines',
            #label='groupclick', 
            opacity = opacity_set1,
            legendgroup = 1,
            hoverinfo = "none",
            name = 'pose_bone',
            line = dict(
                color = color_set1,
                width = width_set1,
                ),    
        ) 
    )
    
    df_plot = df1.iloc[[(slider_value*19-18),(slider_value*19-19),(slider_value*19-17)]]
    fig.add_trace(
        go.Scatter3d(
            x = df_plot['x'],
            y = df_plot['y'],
            z = df_plot['z'],
            mode = 'lines',
            opacity = opacity_set1,
            legendgroup = 1,
            hoverinfo ="none",
            showlegend = False,
            line = dict(
                color = color_set1,
                width = width_set1,
                ),    
        ) 
    )
    
    df_plot = df1.iloc[[(slider_value*19-5),(slider_value*19-6),(slider_value*19-7),(slider_value*19-17),(slider_value*19-13),(slider_value*19-12),(slider_value*19-11),]]
    fig.add_trace(
        go.Scatter3d(
            x = df_plot['x'],
            y = df_plot['y'],
            z = df_plot['z'],
            mode = 'lines',
            opacity = opacity_set1,
            legendgroup = 1,
            hoverinfo ="none",
            showlegend = False,
            line = dict(
                color = color_set1,
                width = width_set1,
                ),    
        ) 
    )
    
    #環境の設定
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=10),#余白left ,right ,bottom,top
                        font_size=10, hoverlabel_font_size=15,
                        width  = 500,
                        height = 500,
                        legend=dict(x=0.01,
                              y=0.99,
                              xanchor='left',
                              yanchor='top',
                              orientation='h',
                              ),
                        scene = dict(##シーン固定
                            xaxis = dict(range=[-1,1],),
                            yaxis = dict(range=[-1,1],),
                            zaxis = dict(range=[-1,1],),
                            xaxis_type="linear", yaxis_type="linear", zaxis_type="linear",
                            xaxis_dtick = 0.5, yaxis_dtick = 0.5, zaxis_dtick = 0.5,
                            aspectmode = "cube",
                            ),
                        scene_camera = dict(#カメラ設定
                                up=dict(x=0, y=0, z=1),
                                center=dict(x=0, y=0, z=0),
                                eye=dict(x=0.9, y=0.9, z=0.9)
                            )
                        )
    return fig