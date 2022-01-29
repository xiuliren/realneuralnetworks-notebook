#using ModernGL

using Makie
# using WGLMakie
# WGLMakie.activate!()
using GLMakie
GLMakie.activate!()

# set_window_config!(;
#     vsync = false,
#     framerate = 30.0,
#     float = false,
#     pause_rendering = false,
#     focus_on_show = false,
#     decorated = true,
#     title = "Makie"
# )


function display3d()

    x = LinRange(0, 10, 100)
    y = sin.(x)
    z = cos.(x)

    fig = lines(x, y, z)

    display(fig)
end

display3d()
