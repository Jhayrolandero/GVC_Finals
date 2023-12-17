  # for i in range(0, 150, 4):  # play around with the steps to generate more or less frames??
    #     i /= 100  # turn values to float
    #     translation.append(pyrr.matrix44.create_from_translation(
    #         [0.6, i, -.1]))  # move the object up for jump effect

    #     # identity since no transformation yet for the letter
    #     trans_above.append(pyrr.matrix44.create_identity(float))
    #     ll_scaling.append(ll_initial_scale)  # scale down the object
    #     # identity since no transformation yet for the letter
    #     trans_back.append(pyrr.matrix44.create_identity(float))
    #     ll_translation.append(pyrr.matrix44.create_from_translation(
    #         ll_position))  # translate to its position (.4, 0, 0)