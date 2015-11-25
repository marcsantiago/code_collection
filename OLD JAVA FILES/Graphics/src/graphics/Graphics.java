/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package graphics;

/**
 *
 * @author marcsantago
 */
import acm.graphics.*;
import acm.program.*;
import java.awt.*;

public class Graphics extends GraphicsProgram {

/** Width of each brick in pixels */
	private static final int BRICK_WIDTH = 30;

/** Width of each brick in pixels */
	private static final int BRICK_HEIGHT = 12;

/** Number of bricks in the base of the pyramid */
	private static final int BRICKS_IN_BASE = 14;
	
	public void run() {
		int totalPyramidWidth = BRICK_WIDTH * BRICKS_IN_BASE;
		int totalPyramidHeight = BRICK_HEIGHT * BRICKS_IN_BASE;
		int startingHeight = getHeight() - 0;
		int startingWidth = (getWidth() - totalPyramidWidth) / 2;
		int size = BRICKS_IN_BASE + 1;
		int x = startingWidth;
		for (int j = 0; j < BRICKS_IN_BASE; j++)
		{
			size--;
			int pyramidWidth = size * BRICK_WIDTH;
			x = (getWidth() - pyramidWidth) / 2;
			startingHeight -= BRICK_HEIGHT;
			for (int i = 0; i < size; i++)
			{
				GRect brick = new GRect(x, startingHeight, BRICK_WIDTH, BRICK_HEIGHT);
                                brick.setFillColor(Color.CYAN);
				add(brick);
				x += BRICK_WIDTH;
			}
		}
	}		
}

