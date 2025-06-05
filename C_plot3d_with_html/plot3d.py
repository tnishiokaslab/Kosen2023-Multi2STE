#https://plotly.com/python/3d-scatter-plots/
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import numpy  as np
import pandas as pd
from makefig import fig_data1_and_2 ,fig_data_human36M

app = Dash(__name__)

txt1 =  'pose_txt\shorin_A_shortpose3d.txt'
txt2 =  'pose_txt\shorin2pose3d.txt'

#↓この辺for文で回したいけど、update_bar_chartで入力指定しないといけないからやり方わからん
out_txt1 = np.loadtxt(txt1)
frame1 = len(out_txt1)//17
out_txt1 = - out_txt1 #画像座標より上下反転

out_txt2 = np.loadtxt(txt2)
frame2 = len(out_txt2)//17
out_txt2 = - out_txt2 #画像座標より上下反転


#グラフ1の色と太さと透明度
color_set1 = 'rgb(0,0,255)'
width_set1 = 10
opacity_set1 = 0.1
#グラフ2の色と太さと透明度
color_set2 = 'rgb(255,0,0)'
width_set2 = 10
opacity_set2 = 0.1


app.layout = html.Div([
    html.H4('三次元姿勢プロット:データ比較'),
    dcc.Graph(id="graph"),
    html.H6("回転角[deg]：",style={'margin': '45px 0 0'}),
    dcc.Slider(         ##回転スライダー
        id='time-slider',
        min=0, max=360, step=1,
        marks={0: '0', 360: '360'},
        value=0,    #初期設定
        tooltip={"placement": "bottom", "always_visible": True},
    ),
    html.H6("動画フレーム："),
    dcc.Slider(         ##スライダー１
        id='time-slider1',
        min=1, max=frame1, step=1,
        marks={1: '1', frame1: str(frame1)},
        value=1,    #初期設定
        tooltip={"placement": "bottom", "always_visible": True},
    ),
    dcc.Slider(         ##スライダー２
        id='time-slider2',
        min=1, max=frame2, step=1,
        marks={1: '1', frame2: str(frame2)},
        value=1,    #初期設定
        tooltip={"placement": "bottom", "always_visible": True},
    ),
    html.Div([
        dcc.Graph(id="graph1",style={"grid-column":"1","grid-row":"1"}),
        dcc.Graph(id="graph2",style={"grid-column":"2","grid-row":"1"}), 
    ],style={"display":"grid","grid_template_columns":"50% 50%"}),
])

@app.callback(#入出力設定
    Output("graph", "figure"), 
    Output("graph1", "figure"), 
    Output("graph2", "figure"), 
    Input("time-slider", "value"),
    Input("time-slider1", "value"),
    Input("time-slider2", "value"),
    )

# def update_bar_chart(slider_value ,slider_value2,IN3):

def update_bar_chart(*args, **kwargs):
    #回転
    rad = np.radians(args[0])
    out_txt2_rot = out_txt2.copy()
    out_txt2_rot[:,0] = out_txt2[:,0]*np.cos(rad) - out_txt2[:,2]*np.sin(rad) 
    out_txt2_rot[:,2] = out_txt2[:,2]*np.cos(rad) + out_txt2[:,0]*np.sin(rad) 
    
    fig_list = []
    fig1 = fig_data_human36M(out_txt1 ,args[1],color_set1 ,width_set1 ,opacity_set1)
    fig2 = fig_data_human36M(out_txt2_rot ,args[2] ,color_set2 ,width_set2 ,opacity_set2)
    fig = fig_data1_and_2(fig1,fig2)
    
    
    
    fig_list.append(fig)
    fig_list.append(fig1)
    fig_list.append(fig2)
    
    return fig_list

app.run_server(debug=True, port = 8800)