import pygame

MIN_SCREEN_SIZE = (600, 300)


def layer_bar(screen: pygame.Surface, font: pygame.font.Font):
    WIDTH = 300
    size = screen.get_size();

    screen.fill((160, 160, 160), (size[0] - WIDTH, 0, WIDTH, size[1]));

    text = font.render("show grid", True, (0, 0, 0));
    textRect = text.get_rect();
    textRect.topleft = (size[0] - WIDTH, 0);
    screen.blit(text, textRect);

    if pygame.mouse.get_pressed()[0]:
        # print("sheeshh")

CANVAS_ITEMS = [
    ((4, 4), (12, 4), (0, 255, 0)),
    ((4, 4), (2, 5), (0, 255, 0)),
    ((12, 4), (10, 5), (255, 0, 0)),
    ((2, 5), (10, 5), (255, 0, 0)),
    ((2, 5), (2, 10), (0, 0, 255)),
    ((10, 5), (10, 10), (0, 0, 255)),
    ((12, 4), (12, 9), (0, 255, 255)),
];

VISUALIZE_LINE = None;
GRID_SIZE = 30;

SHOW_GRID = True;

def canvas(screen: pygame.Surface):
    size = screen.get_size();
    WIDTH = size[0] - 300

    if SHOW_GRID:
        for x in range(0, WIDTH, GRID_SIZE):
            for y in range(0, size[1], GRID_SIZE):
                rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE);
                pygame.draw.rect(screen, (180, 180, 180), rect, 1);

    for item in CANVAS_ITEMS:
        pygame.draw.line(screen, item[2], (item[0][0]*GRID_SIZE, item[0][1]*GRID_SIZE), (item[1][0]*GRID_SIZE, item[1][1]*GRID_SIZE), 4);

    global VISUALIZE_LINE
    if VISUALIZE_LINE:
        pygame.draw.line(screen, (0, 0, 0), (VISUALIZE_LINE[0][0]*GRID_SIZE, VISUALIZE_LINE[0][1]*GRID_SIZE), (VISUALIZE_LINE[1][0]*GRID_SIZE, VISUALIZE_LINE[1][1]*GRID_SIZE), 4);

def main():
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE);
    clock = pygame.time.Clock();

    pygame.font.init();
    font = pygame.font.Font(pygame.font.get_default_font(), 32);
    
    active = True;
    while active:
        clock.tick(60);

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False;
            elif event.type == pygame.VIDEORESIZE:
                width, height = event.w, event.h;
                if width < MIN_SCREEN_SIZE[0]:
                    width = MIN_SCREEN_SIZE[0];
                if height < MIN_SCREEN_SIZE[1]:
                    height = MIN_SCREEN_SIZE[1]

                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE);
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and event.mod & pygame.KMOD_CTRL:
                    print("fuck off ");
                    CANVAS_ITEMS.pop();


        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos();
            global VISUALIZE_LINE
            if VISUALIZE_LINE == None:
                VISUALIZE_LINE = [(round(pos[0] / GRID_SIZE), round(pos[1] / GRID_SIZE)), (round(pos[0] / GRID_SIZE), round(pos[1] / GRID_SIZE)), (0, 0, 0)];
            else:
                VISUALIZE_LINE[1] = round(pos[0] / GRID_SIZE), round(pos[1] / GRID_SIZE);
        else:
            if VISUALIZE_LINE:
                CANVAS_ITEMS.append(VISUALIZE_LINE);
                VISUALIZE_LINE = None;

        screen.fill((220, 220, 220));

        canvas(screen);
        layer_bar(screen, font);

        pygame.display.flip();

if __name__ == '__main__':
    main();