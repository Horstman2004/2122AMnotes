--var = import or require the file 'push'
push = require 'push'
Class = require 'class'
require 'Paddle'
require 'Ball'

WINDOW_WIDTH=1280
WINDOW_HEIGHT=720

VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

PADDLE_SPEED = 200

--A function to start up the window that initialzes the game
function love.load()
     
     --"seed" the RNG so that calls to random are always random
     -- use the current time, since that will vary on startup every time
     math.randomseed(os.time())

     -- use nearest-neighbor filtering on upscaling and downscaling to prevent blurry
     love.graphics.setDefaultFilter('nearest','nearest')
     
     love.window.setTitle('Pong')
     -- var = love's graphics module.newFont('file',fontsize)
     smallFont = love.graphics.newFont('font.ttf',8)
     scoreFont = love.graphics.newFont('font.ttf',32)

     --Sound Table
     sounds = {
          --key = love.audio.newSource('filepath','static')
          ['paddle_hit'] = love.audio.newSource('sounds/paddle_hit.wav','static'),
          ['score'] = love.audio.newSource('sounds/score.wav','static'),
          ['wall_hit'] = love.audio.newSource('sounds/wall_hit.wav','static')
     }

     --this method changes the screen to our virtual resolution
     push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT,{
          fullscreen=false,
          resizable=true,
          vsync=true
     })

     player1Score=0
     player2Score=0
     player3Score=0
     player4Score=0

     player1 = Paddle(10,30,5,20)
     player2 = Paddle(VIRTUAL_WIDTH-10, VIRTUAL_HEIGHT-30, 5, 20)
     player3 = Paddle(VIRTUAL_WIDTH-10, VIRTUAL_HEIGHT-10, 30, 5)
     player4 = Paddle(10, 5, 30, 5)

     ball = Ball(VIRTUAL_WIDTH/2-2,VIRTUAL_HEIGHT/2-2,4,4)
     --this var will help determine what is going on in the game
     --in the beginning, menu, main game, high score, etc
     gameState = 'start'

end



function love.resize(w,h)
     push:resize(w,h)
end


--this f(x) is ran every frame, pass in dt. 
--dt is delta time or change in seconds since the last frame
function love.update(dt)
     --Ball Collision
     if ball:collides(player1) then
          ball.dx = -ball.dx * 1.03
          ball.x = player1.x + 5
          if ball.dy < 0 then
               ball.dy = -math.random(10, 150)
          else
               ball.dy = math.random(10, 150)
          end
          sounds['paddle_hit']:play()
     end

     if ball:collides(player2) then
          ball.dx = -ball.dx * 1.03
          ball.x = player2.x + 5
          if ball.dy < 0 then
               ball.dy = -math.random(10, 150)
          else
               ball.dy = math.random(10, 150)
          end
          sounds['paddle_hit']:play()
     end

     if ball:collides(player3) then
          ball.dx = -ball.dx * 1.03
          if ball.dy < 0 then
               ball.dy = math.random(10, 150)
          else
               ball.dy = -math.random(10, 150)
          end
          sounds['paddle_hit']:play()
     end

     if ball:collides(player4) then
          ball.dx = -ball.dx * 1.03
          if ball.dy < 0 then
               ball.dy = math.random(150, 260)
          else
               ball.dy = -math.random(150, 260)
          end
          sounds['paddle_hit']:play()
     end

     -- if we reach the left or right edge of the screen, 
     -- go back to start and update the score
     if ball.x < 0 then
          sounds['score']:play()
          servingPlayer = 1
          player2Score = player2Score + 1
          ball:reset()
          gameState = 'serve'
     end

     if ball.x > VIRTUAL_WIDTH then
          sounds['score']:play()
          servingPlayer = 2
          player1Score = player1Score + 1
          ball:reset()
          gameState = 'serve'
     end     

     if ball.y > VIRTUAL_HEIGHT then
          sounds['score']:play()
          servingPlayer = 4
          player3Score = player3Score + 1
          ball:reset()
          gameState = 'serve'
     end     

     if ball.y < 0 then
          sounds['score']:play()
          servingPlayer = 3
          player4Score = player4Score + 1
          ball:reset()
          gameState = 'serve'
     end     
     --player 1 movement
     if love.keyboard.isDown('w') then
          -- move up by add a negative paddle speed to the y scaled by dt
         player1.dy = -PADDLE_SPEED
     elseif love.keyboard.isDown('s') then
          -- move down by add a positive paddle speed to the y scaled by dt
          player1.dy = PADDLE_SPEED
     else
          player1.dy = 0
     end

     --player 2 movement
     if love.keyboard.isDown('e') then
          -- move up by add a negative paddle speed to the y scaled by dt
          player2.dy = -PADDLE_SPEED
     elseif love.keyboard.isDown('d') then
          -- move down by add a positive paddle speed to the y scaled by dt
          player2.dy = PADDLE_SPEED
     else
          player2.dy = 0
     end

     if love.keyboard.isDown('k') then
          -- move up by add a negative paddle speed to the y scaled by dt
          player3.dx = -PADDLE_SPEED
     elseif love.keyboard.isDown('l') then
          -- move down by add a positive paddle speed to the y scaled by dt
          player3.dx = PADDLE_SPEED
     else
          player3.dx = 0
     end

     if love.keyboard.isDown('i') then
          -- move up by add a negative paddle speed to the y scaled by dt
          player4.dx = -PADDLE_SPEED
     elseif love.keyboard.isDown('o') then
          -- move down by add a positive paddle speed to the y scaled by dt
          player4.dx = PADDLE_SPEED
     else
          player4.dx = 0
     end

     --ball movement
     if gameState == 'play' then
          --scale the velocity by dt so movement is framerate-independent
          ball:update(dt)
     end
     
     player1:update(dt)
     player2:update(dt)
     player3:update(dt)
     player4:update(dt)
     


     ball:update(dt)
end

--Check for any keypressing
function love.keypressed(key)
     -- keys can be access by string name
     if key=='escape' then
          love.event.quit()  --this will close the window
     elseif key == 'enter' or key == 'return' then
          if gameState == 'start' then
               gameState='play'
          else
               gameState='start'
               ball:reset()
          end
     end
end

--draw on the screen the letters
--update the screen with information:  draw anything that is needed
function love.draw()
     --begin rendering at a virtual resolution
     push:apply('start')

     --clear the screen and reset the background color
     --love.graphics.clear(r,g,b,a)
     love.graphics.clear(40,45,52,255)
     --set font for love
     love.graphics.setFont(smallFont)

     if gameState == 'start' then
          love.graphics.printf('Hello Start State!',0,20,VIRTUAL_WIDTH,'center')
     else
          love.graphics.printf('Hello Play State!',0,20,VIRTUAL_WIDTH,'center')
     end

     love.graphics.setFont(scoreFont)
     love.graphics.print(tostring(player1Score),VIRTUAL_WIDTH/2-50,VIRTUAL_HEIGHT/3)
     love.graphics.print(tostring(player2Score),VIRTUAL_WIDTH/2+50,VIRTUAL_HEIGHT/3)
     love.graphics.print(tostring(player3Score),VIRTUAL_WIDTH/2-50,VIRTUAL_HEIGHT/2)
     love.graphics.print(tostring(player4Score),VIRTUAL_WIDTH/2+50,VIRTUAL_HEIGHT/2)

     -- Draw the paddles and the ball
     player1:render()
     player2:render()
     player3:render()
     player4:render()
     ball:render()

     displayFPS()
     --end virtual resolution
     push:apply('end')
end



--anything that is not a love function put a th e bottom
function displayFPS()
     love.graphics.setFont(smallFont)
     love.graphics.setColor(0,255,0,255)
     love.graphics.print('FPS: ' ..tostring(love.timer.getFPS()),10,10)
end