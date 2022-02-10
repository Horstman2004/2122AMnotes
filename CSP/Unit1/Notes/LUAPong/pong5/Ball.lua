Ball = Class{}
local gameState

function Paddle:init(x,y,dx,dy)
    self.ballx = x
    self.bally = y 
    self.balldx = dx
    self.balldy = dy
end

function Paddle:update(dt)
    --check to see if we are going up or down
    if gameState == 'start' then
        gameState='play'
    else
        gameState='start'
        self.ballx = VIRTUAL_WIDTH / 2 - 2
        self.bally = VIRTUAL_HEIGHT / 2 - 2
        self.balldx = math.random(2) == 1 and 100 or -100
        self.balldy = math.random(-50,50)
    end
end


function Paddle:render()
    love.graphics.rectangle('fill',self.ballx,self.bally,self.balldx,self.balldy)
end