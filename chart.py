import plotly.express as px
import plotly.graph_objects as go


def create_pie_chart(df, column_name, title, mapping):
    grouped_df = df.groupby(by=[column_name], as_index=False)['Group'].count()

    custom_label = grouped_df[column_name].map(mapping)

    grouped_df['custom label'] = custom_label

    total_value = grouped_df['Group'].sum()

    fig = go.Figure(data = [go.Pie(
        labels=grouped_df['custom label'],
        values=grouped_df['Group'],
        textposition='inside',
        hole=.33,
        textinfo='percent',
        hoverinfo='label+value',
        direction='clockwise',
        marker=dict(
            colors=px.colors.sequential.Plasma
        )
    )])
    fig.update_layout(
        title = title,
        showlegend=False,
        annotations = [
            dict(
                x=1.0,
                y=1.05,
                xref = 'paper',
                yref = 'paper',
                text=f'Total: {total_value}',
                showarrow=False,
                font=dict(size=19),
                align='left',
            )
        ]
    )
    return fig
