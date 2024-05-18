def team_pts(wins, losses, ot_losses):
    print('wins:', wins)
    print('losses:', losses)
    print('ot_losses:', ot_losses)
    print('total points:')
    return (2 * wins) + (1 * ot_losses)


team_pts(10, 9, 3)
