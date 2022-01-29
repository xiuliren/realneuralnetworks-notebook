using GLMakie
legendentries = Dict("A" => LineElement(linestyle = nothing, linewidth = 0.3, color = :red),
                     "B" => MarkerElement(color = :white, marker = '⋆', strokecolor = :black, markerstrokewidth = 0.5, strokewidth = 0.5, markersize = 10px))
fig = Figure()
ax = fig[1, 1] = Axis(fig, aspect = DataAspect(), xlabel = "X (cm)", ylabel = "Y (cm)")
lines!(ax, rand(Point2f0, 10)) # Iwant the line here to be red and have a thickness of 0.3
scatter!(ax, rand(Point2f0, 10)) # I want the markers here to be stars etc...
fig[0,1] = Legend(fig, collect(values(legendentries)), collect(keys(legendentries)))
fig
