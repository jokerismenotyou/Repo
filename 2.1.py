from pyecharts.charts import Line
import pyecharts.options as opts

# 创建阶梯图对象
line = (
    Line()
    .add_xaxis(["1995", "1996", "1997", "1998", "1999", "2000",
                "2001", "2002", "2003", "2004", "2005", "2006",
                "2007", "2008", "2009"])
    .add_yaxis("1995-2009年美国邮票价格",
               [0.32, 0.32, 0.32, 0.32, 0.33, 0.33, 0.34, 0.37,
                0.37, 0.37, 0.37, 0.39, 0.41, 0.42, 0.44],
               is_step=True,  # 设置为阶梯图
               linestyle_opts=opts.LineStyleOpts(width=3, color='green'),  # 设置线条样式
               label_opts=opts.LabelOpts(font_size=12),  # 设置标签字体大小
               )
    .set_global_opts(
        title_opts=opts.TitleOpts(title='1995-2009年美国邮票价格'),  # 更改标题
        yaxis_opts=opts.AxisOpts(min_=0.2, max_=0.5)
    )
)

line.render("D:\\text1.html")  # 将阶梯图保存到 D 盘


from pyecharts.charts import Line
import pyecharts.options as opts

# 创建折线图对象
line = (
    Line()
    .add_xaxis(["1995", "1996", "1997", "1998", "1999", "2000",
                "2001", "2002", "2003", "2004", "2005", "2006",
                "2007", "2008", "2009"])
    .add_yaxis("1995-2009年美国邮票价格",
               [0.32, 0.32, 0.32, 0.32, 0.33, 0.33, 0.34, 0.37,
                0.37, 0.37, 0.37, 0.39, 0.41, 0.42, 0.44],
               is_step=False,  # 设置为折线图
               linestyle_opts=opts.LineStyleOpts(width=3, color='green'),  # 设置线条样式
               label_opts=opts.LabelOpts(font_size=12),  # 设置标签字体大小
               )
    .set_global_opts(
        title_opts=opts.TitleOpts(title='1995-2009年美国邮票价格'),  # 更改标题
        yaxis_opts=opts.AxisOpts(min_=0.2, max_=0.5)
    )
)

line.render("D:\\text2.html")  # 将折线图保存到 D 盘
