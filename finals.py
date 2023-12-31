import numpy as np
import pyrr
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import glfw
from PIL import Image


def main():
    # Shaders
    vertex_src = """
    # version 330

    layout(location = 0) in vec3 position;
    layout(location = 1) in vec3 color;
    layout(location = 2) in vec2 texCoord;

    uniform mat4 model;

    out vec3 v_color;
    out vec2 out_texCoord;

    void main()
    {
        gl_Position = model * vec4(position, 1.0);
        v_color = color;
        out_texCoord = texCoord;
    }
    """

    fragment_src = """
    # version 330

    in vec3 v_color;
    in vec2 out_texCoord;

    uniform sampler2D texture1;

    out vec4 out_color;

    void main()
    {
        //out_color = vec4(v_color, 1.0) * texture(texture1, out_texCoord); //blending for color effect
        out_color = texture(texture1, out_texCoord); //applying texture
    }
    """

    # glfw window initialization
    glfw.init()
    window = glfw.create_window(800, 600, "My First Render", None, None)

    if not window:
        glfw.terminate()
        exit()

    glfw.make_context_current(window)

    # local space/object creation
    # vertices coordinates
    vertices = [-0.5, 0.5, -0.0, 1.0, 0.0, 0.0, 0, 0,  # 0 r
                -0.5, -0.5, -0.0, 0.0, 1.0, 0.0, 0, 1,  # 1 g    1   2   5   6
                0.5, -0.5, -0.0, 0.0, 0.0, 1.0, 1, 1,  # 2 b
                0.5, 0.5, -0.0, 1.0, 0.0, 1.0, 1, 0]  # 7 r
    vertices = np.array(vertices, dtype=np.float32)

    indices = [0, 1, 2, 0, 2, 3]
    indices = np.array(indices, dtype=np.uint32)

    # sending/binding data to the gpu
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)
    # vbo
    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
    # vertex
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(0))
    # color
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(12))
    # texture
    glEnableVertexAttribArray(2)
    glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(24))
    # indexing
    ebo = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER,
                 indices.nbytes, indices, GL_STATIC_DRAW)
    glBindVertexArray(0)

    # A
    # vao
    vao_a = glGenVertexArrays(1)
    glBindVertexArray(vao_a)

    # vbo
    vbo_a = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo_a)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    # vertex
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(0))

    # color
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(12))

    # texture
    glEnableVertexAttribArray(2)
    glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(24))

    # indexing
    ebo_a = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo_a)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER,
                 indices.nbytes, indices, GL_STATIC_DRAW)
    glBindVertexArray(0)

    # C
    # vao
    vao_c = glGenVertexArrays(1)
    glBindVertexArray(vao_c)

    # vbo
    vbo_c = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo_c)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    # vertex
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(0))

    # color
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(12))

    # texture
    glEnableVertexAttribArray(2)
    glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(24))

    # indexing
    ebo_c = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo_c)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER,
                 indices.nbytes, indices, GL_STATIC_DRAW)
    glBindVertexArray(0)

    # E
    # vao
    vao_e = glGenVertexArrays(1)
    glBindVertexArray(vao_e)

    # vbo
    vbo_e = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo_e)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    # vertex
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(0))

    # color
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(12))

    # texture
    glEnableVertexAttribArray(2)
    glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(24))

    # indexing
    ebo_e = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo_e)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER,
                 indices.nbytes, indices, GL_STATIC_DRAW)
    glBindVertexArray(0)

    # L --
    vao_l = glGenVertexArrays(1)
    glBindVertexArray(vao_l)
    # vbo1
    vbo_l = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo_l)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
    # vertex
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(0))
    # color
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(12))
    glEnableVertexAttribArray(2)
    glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(24))
    # indexing
    ebo_l = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo_l)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER,
                 indices.nbytes, indices, GL_STATIC_DRAW)
    glBindVertexArray(0)

    img = Image.open("LetterL.png")
    img_data = np.array(list(img.getdata()), np.uint8)
    glActiveTexture(GL_TEXTURE1)  # location 1
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.width, img.height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,
                    GL_LINEAR_MIPMAP_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glGenerateMipmap(GL_TEXTURE_2D)

    img1 = Image.open("Meteor.png")
    img_data1 = np.array(list(img1.getdata()), np.uint8)
    glActiveTexture(GL_TEXTURE2)  # location 2
    texture1 = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture1)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img1.width,
                 img1.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data1)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,
                    GL_LINEAR_MIPMAP_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glGenerateMipmap(GL_TEXTURE_2D)

    img_a = Image.open("LetterA.png")
    img_data_a = np.array(list(img_a.getdata()), np.uint8)
    glActiveTexture(GL_TEXTURE3)  # Location 3 for the new texture
    texture_a = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_a)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img_a.width,
                 img_a.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data_a)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,
                    GL_LINEAR_MIPMAP_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glGenerateMipmap(GL_TEXTURE_2D)

    img_c = Image.open("LetterC.png")
    img_data_c = np.array(list(img_c.getdata()), np.uint8)
    glActiveTexture(GL_TEXTURE4)  # Location 4 for the new texture
    texture_c = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_c)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img_c.width,
                 img_c.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data_c)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,
                    GL_LINEAR_MIPMAP_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glGenerateMipmap(GL_TEXTURE_2D)

    img_e = Image.open("LetterE.png")
    img_data_e = np.array(list(img_e.getdata()), np.uint8)
    glActiveTexture(GL_TEXTURE6)  # Location 5 for the new texture
    texture_g = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_g)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img_e.width,
                 img_e.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data_e)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,
                    GL_LINEAR_MIPMAP_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glGenerateMipmap(GL_TEXTURE_2D)

    # TRANSFORMATIONS
    # trans1 = pyrr.matrix44.create_from_translation([-8, 0, 0])
    # trans2 = pyrr.matrix44.create_from_translation([-4, 0, 0])
    # trans3 = pyrr.matrix44.create_from_translation([0, 0, 0])
    # trans4 = pyrr.matrix44.create_from_translation([4, 0, 0])
    model_a = pyrr.matrix44.create_from_translation([-0.6, 0.00, -0.2])
    let_scale = pyrr.matrix44.create_from_scale([0.5, 0.5, 0.5])

    model_c = pyrr.matrix44.create_from_translation([-0.20, 0.00, -0.2])

    model_e = pyrr.matrix44.create_from_translation([0.20, 0.00, -0.2])

    # scale5 = pyrr.matrix44.create_from_scale([.5, .5, 1])
    # trans5 = pyrr.matrix44.create_from_translation([.8, 0, 0])

    ll_position = [.6, 0.00, 0]
    ll_initial_scale = pyrr.matrix44.create_from_scale([0.5, 0.5, 0.5])
    scale = pyrr.matrix44.create_from_scale([0.5, 0.5, 0.5])

    # loop to create frames from left to right
    # empty lists for frames
    translation = []  # lamp translations #frames holder
    # letter transformations
    # translate the object above the origin for squishing down instead of collapsing
    trans_above = []
    ll_scaling = []  # declare an empty list for scaling the letter
    trans_back = []  # translate back to origin after scaling
    ll_translation = []  # translate to position

    # Generate matrices to translate the lamp from left (-.8) to right (.4)
    for i in range(-130, 61, 3):  # play around with the steps to generate more or less frames??
        i /= 100
        for _ in range(2):  # create 2 frames of the same value for staying effect
            translation.append(pyrr.matrix44.create_from_translation(
                [i, 0.5, -.1]))  # i = -.8 to .4 skipping by a factor of .02

            # identity since no transformation yet for the letter
            trans_above.append(pyrr.matrix44.create_identity(float))
            # scale down the object since object vertices makes it bigger
            ll_scaling.append(ll_initial_scale)
            # identity since no transformation yet for the letter
            trans_back.append(pyrr.matrix44.create_identity(float))
            ll_translation.append(pyrr.matrix44.create_from_translation(
                ll_position))  # translate to its position (.4, 0, 0)

    # Squish
    for i in range(0, 6, 1):  # play around with the steps to generate more or less frames??
        for _ in range(3):  # create 3 frames of the same value for staying effect
            translation.append(pyrr.matrix44.create_from_translation(
                [.6, .5 - i/20, -.1]))  # move the object down for falling effect
            # translate object above the origin for squishing effect instead of collapsing
            trans_above.append(
                pyrr.matrix44.create_from_translation([0, .5, 0]))
            ll_scaling.append(pyrr.matrix44.multiply(ll_initial_scale, pyrr.matrix44.create_from_scale(
                [1, (5-i)/5, 1])))  # scale down for squish effect
            trans_back.append(pyrr.matrix44.create_from_translation(
                [0, - (((6 - i)/6) / (6-i)), 0]))  # translate back to origing
            ll_translation.append(pyrr.matrix44.create_from_translation(
                ll_position))  # translate to its position (.4, 0, 0)

    # Continue to the right
    for i in range(6, 60, 1):
        translation.append(pyrr.matrix44.create_from_translation(
            [i/10, 0, -.1]))  # continue going to the right
        # same as identity since no more transformation
        trans_above.append(pyrr.matrix44.create_from_translation([0, 0, 0]))
        ll_scaling.append(pyrr.matrix44.multiply(
            ll_initial_scale, pyrr.matrix44.create_from_scale([1, (5-6)/5, 1])))
        # same as identity since no more transformation
        trans_back.append(pyrr.matrix44.create_from_translation([0, 0, 0]))
        ll_translation.append(pyrr.matrix44.create_from_translation(
            [.6, -.15, 0]))  # translate to its position (.4, 0, 0)

    # SHADER SPACE
    shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER),
                            compileShader(fragment_src, GL_FRAGMENT_SHADER))
    glUseProgram(shader)
    model_loc = glGetUniformLocation(shader, 'model')
    tex_loc = glGetUniformLocation(shader, "texture1")

    # RENDERING LOOP
    glClearColor(0.1, 0.1, 0.1, 1)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)  # for transparency and coloring effect
    # for transparency and coloring effect
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    i = 0

    while not glfw.window_should_close(window):
        glfw.poll_events()  # get all events
        # set the buffer color set in the glClearColor function
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Multiplying the matrices
        model = trans_above[i]  # Goes up
        # print("transdt")
        # print(model)
        model = pyrr.matrix44.multiply(
            model, ll_scaling[i])  # Scaling for squish effect
        # print("scaledt")
        # print(model)
        model = pyrr.matrix44.multiply(model, trans_back[i])  # Goes down
        # print("backedt")
        # print(model)
        model = pyrr.matrix44.multiply(
            model, ll_translation[i])  # Goes back to old position
        # print("model")
        # print(model)
        # Rendering the letter

        # Rendering the letter L
        glBindVertexArray(vao_l)
        glUniform1i(tex_loc, 1)  # use location 1
        glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
        glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

        # Rendering the letter A
        model = pyrr.matrix44.multiply(let_scale, model_a)
        glBindVertexArray(vao_a)
        glUniform1i(tex_loc, 3)  # use location 3
        glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
        glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

        # Rendering the letter C
        model = pyrr.matrix44.multiply(let_scale, model_c)
        glBindVertexArray(vao_c)
        glUniform1i(tex_loc, 4)  # use location 4
        glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
        glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

        # Rendering the letter E
        model = pyrr.matrix44.multiply(let_scale, model_e)
        glBindVertexArray(vao_e)
        glUniform1i(tex_loc, 6)  # use location 5
        glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
        glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

        glEnable(GL_DEPTH_TEST)

        # Rendering the meteor
        model = pyrr.matrix44.multiply(scale, translation[i])
        glBindVertexArray(vao)
        glUniform1i(tex_loc, 2)  # use location 2
        glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
        glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

        glDisable(GL_DEPTH_TEST)

        # List iterator of frames
        if i >= len(translation) - 1:
            i = 0
        else:
            # iterate by one. #for kawaii efect :D (i = i+1 or i += 1) #can be used to skip frames?
            i -= -1

        # swap the next buffer
        # intervals before swapping frames. higher values = slower
        glfw.swap_interval(2)
        glfw.swap_buffers(window)

    # object deletion
    glDeleteProgram(shader)
    glDeleteVertexArrays(1, (vao, vao_l, vao_a, vao_c, vao_e))
    glDeleteBuffers(3, (vbo, ebo, vbo_a, vbo_c, vbo_e))
    glDeleteTextures(3, (texture1, texture, texture_a, texture_c, texture_g))
    glfw.terminate()


if __name__ == '__main__':
    main()
