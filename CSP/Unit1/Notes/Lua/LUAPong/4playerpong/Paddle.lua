-- class Paddle:  for python
Paddle = Class{}

-- 'init' function or Constructor
-- def __init__(self,x,y,width,height):
--        self.x = x
function Paddle:init(x, y, width, height)
     self.x = x
     self.y = y
     self.width = width
     self.height = height
     self.dx = 0
     self.dy = 0
end
 
function Paddle:update(dt)
     if self.dy < 0 then
         self.y = math.max(0, self.y + self.dy * dt)
     elseif self.dx < 0 then
          self.x = math.max(0, self.x + self.dx * dt)
     else
         self.y = math.min(VIRTUAL_HEIGHT - self.height, self.y + self.dy * dt)
         self.x = math.min(VIRTUAL_WIDTH - self.width, self.x + self.dx * dt)
     end
end

-- Paddle will need to be drawn or render
function Paddle:render()
     love.graphics.rectangle('fill',self.x,self.y,self.width,self.height)
end