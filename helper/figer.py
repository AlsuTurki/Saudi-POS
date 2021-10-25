#not used 

fig = go.Figure(data=go.Scattergeo( lon = Grouped_City['location_longitude'], lat = Grouped_City['location_latitude'],
        text = Grouped_City['text'], mode = 'markers', marker = dict(size = 8, opacity = 0.8, reversescale = True,
            autocolorscale = False, symbol = 'square', line = dict( width=1, color='rgba(102, 102, 102)'),
            colorscale = 'Blues', cmin = 0, color = Grouped_City['Value of Transactions'], cmax = Grouped_City['Value of Transactions'].max(),
            colorbar_title="Value of Transactions" )
        ))
fig.update_layout(
        #title = 'المدن',
        geo = dict(resolution = 50, scope = 'asia', showframe = False, showcoastlines = True,
        showland = True, landcolor = "rgb(229, 229, 229)", countrycolor = "rgb(255, 255, 255)" , 
        coastlinecolor = "rgb(255, 255, 255)", projection = dict( type = 'mercator', scale=4),
        center = dict(lon=46, lat=24)
    ))
#fig.show()
fig