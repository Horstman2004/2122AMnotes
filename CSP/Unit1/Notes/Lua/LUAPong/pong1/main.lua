--var = import or require the file 'push'
push = require 'push'

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

--A function to start up a windwo that initializes the game
function love.load()

    love.graphics.setDefaultFilter('nearest','nearest')

    -- Method changes the sscreen to our virtual resolution
    push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT,{
        fullscreen = false,
        resizable = true,
        vsync = true
    })
end

--Check for any keypressing
function love.keypressed(key)
    --keys can be accessed by string name
    if key=='escape' then
        love.event.quit()
    end
end

--draw on the screen the letters
--update the screen with the infromation:  draw anything that is needed
function love.draw()
    -- begin rending at a virtual resolution
    push:apply('start')

    love.graphics.printf(
        'Hello Pong!',              --text to render
        0,                          --starting X
        VIRTUAL_HEIGHT/2,            --starting Y
        VIRTUAL_WIDTH,               -- number of pixels to center within
        'center'                    --alignment
    )
    --end virtual resolution
    push:apply('end')
end