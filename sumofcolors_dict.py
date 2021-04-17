def get_colors_score(ball_list):
    colors_score_dict={}
    for item in ball_list:
        pair=item.split(":")
        color,score=pair[0],int(pair[1])
        if color in colors_score_dict:
            colors_score_dict[color]=colors_score_dict[color]+score
        else:
            colors_score_dict[color]=score
    return colors_score_dict





ball_list=input().split(",")
print(get_colors_score(ball_list))
