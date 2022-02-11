Ball = Class{}
push = require 'push'
Class = require 'class'
require 'Paddle'

function Ball:init(x,y,width,height)
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    -- these var are keeping track of our velocity on both
    -- X and Y axis, since the ball can move in two dimensions
    self.dy = math.random(2) == 1 and - 100 or 100
    self.dx = math.random(-50,50)
end

--Places the ball in the middle of the screen, with an initial random velocity scalled by delta time
function Ball:reset()
    self.x = VIRTUAL_WIDTH/2-2
    self.y = VIRTUAL_HEIGHT/2-2
    self.dy = math.random(2) == 1 and - 100 or 100
    self.dx = math.random(-50,50)
end

function Ball:collides(paddle)
    if self.x > paddle.x + paddle.w or paddle.x > self.x + self.width then
        return false
    end

    if self.y > paddle.y + paddle.h or paddle.y > self.y + self.height then
        return false
    end

    return true
end

--Simply applies velocity to position, scaled by delta time
function Ball:update(dt)
    self.x = self.x + self.dx * dt
    self.y = self.y + self.dy * dt
end

function Ball:render()
    love.graphics.rectangle('fill',self.x,self.y,self.width,self.height)
end