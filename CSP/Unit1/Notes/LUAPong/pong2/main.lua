--var = import or require the file 'push'
push = require 'push'

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

--A function to start up a window that initializes the game
function love.load()

    love.graphics.setDefaultFilter('nearest','nearest')

    --var = love's graphics module.newfont('file',fontsize)
    smallFont = love.graphics.newFont('font.ttf',8)
    --set font for love
    love.graphics.setFont(smallFont)

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

    --clear the screen and reset the background color
    --love.graphics.clear(r,g,b,a)
    love.graphics.clear(40,45,52,255)

    love.graphics.printf('Hello Pong!',0,20,VIRTUAL_WIDTH,'center')

    --Draw the paddles and the ball

    --love.graphics.setting.rectangle('filled or not',x,y,width,height)
    love.graphics.rectangle('fill',10,30,5,20)
    --second paddle
    love.graphics.rectangle('fill',VIRTUAL_WIDTH-10,VIRTUAL_HEIGHT-50,5,20)
    --render ball
    love.graphics.rectangle('fill',VIRTUAL_WIDTH/2-2,VIRTUAL_HEIGHT/2-2,4,4)
    --end virtual resolution
    push:apply('end')
end