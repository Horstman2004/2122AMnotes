WINDOW_WIDTH=1280
WINDOW_HEIGHT=720


function love.load()
    love.graphics.setDefaultFilter('nearest','nearest')
    love.window.setTitle('Lua Clock')
    timeFont = love.graphics.newFont(64)
end


function love.draw()
    love.graphics.clear(40,45,52,255)
    love.graphics.print(os.date())
    love.graphics.setFont(timeFont)
end
