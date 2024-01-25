import random
import csv
import itertools
import tkinter as tk

class G_object():
    # create objects to represent the graphics with inventory object number, title, height, width, assignment to size group small, color for depiction  in GUI
    def __init__(self, objectnumber, title, height, width, small, color):
        self.nr = objectnumber
        self.title = title
        self.height = float(height)
        self.width = float(width)
        self.small = small
        self.color = str(color)

class G_individual():
    # create objects to represent the graphics with inventory object number, title, height, width, assignment to size group small, color for depiction  in GUI, group number and size of passepartout
    def __init__(self, nr, title, height, width, small, color, outer_h, outer_w, outer_fr_h, outer_fr_w):
        self.nr = nr
        self.title = title
        self.height = float(height)
        self.width = float(width)
        self.small = small
        self.color = str(color)
        self.gr = 0
        self.pp_inner_h = float(height) + 0.8
        #Fenstermaß Höhe
        self.pp_inner_w = float(width) + 0.8
        #Fenstermaß Breite
        self.pp_outer_h = float(outer_h)
        self.pp_outer_w = float(outer_w)
        self.frame_inner_h = float(outer_h)
        self.frame_inner_w = float(outer_w)
        self.frame_outer_h = float(outer_fr_h)
        self.frame_outer_w = float(outer_fr_w)


def create_objects(grouping_t):
    graphics_list = []
    colorcodelist = ['#DAF7A6', '#FFC300', '#FF5733', '#C70039', '#900C3F', '#ff0000', '#0fb3f0', '#f1b000', '#ffd78f', '#319938', '#da2528', '#3061e3', '#1e588f', '#298a0c', '#733e98', '#6e4e8e', '#c9c9ff', '#008000', '#993920', '#d0d3d5', '#e6aabb', '#d793a9', '#a77fb3', '#7d4737', '#ff4438', '#ccff00', '#7df9ff', '#f0ead6', '#76eec6', '#e30b5d', '#01d27a', '#b2ec73', '#2e0519', '#23bd29', '#00adec', '#0187ce', '#1c70c2', '#eb0e99', '#7a056c', '#70e7a2', '#453bba', '#29db4f', '#ff8241', '#3287da', '#fe3332', '#ad206a', '#530958']
    # list of colors which will be attached to the graphics in tkinter GUI
    with open('MLgraphiclist.csv', 'r') as f:
        # read csv file
        reader = csv.reader(f, delimiter=';',)
        next(reader)
        for i, row in enumerate(reader):
            # add boolean value to decide if the graphics get a small or big passepartout
            if ( float(row[2]) < grouping_t) or (float(row[3]) < grouping_t):
                small = True
            else:
                small = False
            if i < len(colorcodelist):
                # add color to every graphic
                color = colorcodelist[i]
            else:
                color =  '#C2B280'
            graphics_list.append(G_object(row[0], row[1], row[2], row[3], small, color))
            # create objects for graphics and add to list
    return graphics_list

def randomize_lists(l):
    #permutations = list(itertools.permutations(l))
    #return permutations
    #Workig with the solution above would give an optimal result, but is too much computing power for my laptop, therefore "only" 5000 versions of the list will be returned
    shuffled_lists=[]
    for i in range(5000):
        ls=l.copy()
        random.shuffle(ls)
        shuffled_lists.append(ls)
        # create list with 5000 random shuffled versions of the list of graphic objects
    return shuffled_lists

def get_result(shuffled_lists, precision, output):
    for l in shuffled_lists:
        # find possible combinations of graphics by comparing their heights and widths in the shuffled lists
        ind_objects = []
        ind_objects.append(l[0])
        startH = l[0].height
        startW = l[0].width
        for gr in l:
            if gr in ind_objects:
                pass
            elif (startH < gr.height < (startH + precision)):
                if (startW < gr.width < (startW + precision)):
                    ind_objects.append(gr)
                    # appends result if the height and width of the graphic is in the defined range (precision)
                else:
                    pass
            else:
                pass
        if len(ind_objects)>1:
            # turn result into set and add it to the final results if it's not already included
            ind_objects = set(ind_objects)
            if ind_objects not in output:
                output.append(ind_objects)
    return output

def clear_result(res):
    # Remove all results that are already part of a larger result group
    for r in res:
        for re in res:
            if (len(r.intersection(re)) == len(re)) or (len(r.intersection(re)) == len(r)):
                if len(re) < len(r):
                    res.remove(re)
                elif len(r) < len(re):
                    res.remove(r)
                    continue     
            else:
                continue
    return res

def ordergroups(groupsets):
    # sort groups by length and add numbering to the group
    i=0
    groups = []
    pgroups = groupsets.sort(key=len, reverse=True)
    for gr in groupsets:
        i = i+1
        for g in gr:
            g.nr = i
    return groupsets

def pp_details(groups):
    new_groups = []
    for group in groups:
        # finds the largest width and height for every group of graphics
        new_group = []
        # list for groups with graphic objects of class G_individual
        maxheight = max(g.height for g in group)
        maxwidth = max(g.width for g in group)
        for g in group:
            if g.small == True:
                g_new = G_individual(g.nr, g.title, g.height, g.width, g.small, g.color, maxheight + 12.8, maxwidth + 12.8, maxheight+14.8, maxwidth+14.8)
                # create new objects with passepartout dimensions
                new_group.append(g_new)
            else:
                g_new = G_individual(g.nr, g.title, g.height, g.width, g.small, g.color, maxheight + 14.8, maxwidth + 14.8, maxheight+16.8, maxwidth+16.8)
                # create new objects with passepartout dimensions
                new_group.append(g_new)
        new_groups.append(new_group)
        # create list of G_individual object groups
    return new_groups

def create_gui(result):
    window = tk.Tk()
    # Create tkinter window
    window.geometry("600x600")
    window.configure(bg='#e1e7fa')
    # configure colour for window
    columncount = max(len(r)for r in result)
    rowcount = len(result)
    # define length of columns and rows depending on the results
    title = tk.Label(window, text="Passepartout Planungstool", justify='center', font='bold')
    # add label to window
    title.grid(row=0, columnspan=columncount)
    # center position for title
    pp_frame=tk.Frame(window)
    # create tkinter frame
    for i, grgroup in enumerate(result):
        # create grid for every group of graphics in the results
        pp_c = tk.Canvas(pp_frame, width=(columncount * 600 + 600), height=(rowcount * 300))
        # create tkinter Canvas in frame to present the results
        pp_c.grid()
        for gr in grgroup:
            if gr.small == True:
                tk.Label(borderwidth=2, relief='solid', bg='#eabbf0', text=f"""Mögliche Gruppe {i+1}: \n Passepartout 6 cm""").grid(row=i+1, column=0, padx=5, pady=1)
                # create label for small group result (< grouping threshold)
            else:
                tk.Label(borderwidth=2, relief='solid', bg='#7593f0', text=f"""Mögliche Gruppe {i+1}: \n Passepartout 7 cm""").grid(row=i+1, column=0, padx=5, pady=1)
                # create label for big group result (> grouping threshold)
        for j, gr in enumerate(grgroup):
            tk.Label(borderwidth=1, relief='solid', bg=gr.color, text=f"""{gr.title} \n {gr.height} x {gr.width} cm \n PP Höhe innen: {round(gr.pp_inner_h, 1)} cm PP Breite innen: {round(gr.pp_inner_w, 1)} cm \n PP Höhe außen: {round(gr.pp_outer_h, 1)} cm PP Breite außen: {round(gr.pp_outer_w, 1)} cm \n Rahmenhöhe innen: {round(gr.frame_inner_h, 1)} cm Rahmenbreite innen: {round(gr.frame_inner_w, 1)} cm \n Rahmenhöhe außen: {round(gr.frame_outer_h, 1)} cm Rahmenbreite außen: {round(gr.frame_outer_w, 1)} cm """).grid(row=i+1, column=j+1, padx=10, pady=10)
            # add detailed information for every graphic with detailed Passepartout size
    window.mainloop()
    # run tkinter application
    return window

if __name__ == "__main__":
    grouping_threshold = 40
    # define the threshold for the grouping of small and bis graphics in cm
    precision = 2
    # define the threshold for the graphic size which can be in the same group for one size of frame in cm
    output = []
    start_list = create_objects(grouping_threshold)
    # read list and create python objects for every graphic in the list
    shuffled_lists = randomize_lists(start_list)
    # shuffle list of graphic objects to find the best groups of graphics
    result = get_result(shuffled_lists, precision, output)
    # find possible combinations of graphics for the given grouping threshold and precision value
    result = clear_result(result)
    # removes groups from result which are already given in bigger groups of graphics
    result = ordergroups(result)
    # order groups from biggest to smalles groups
    result = pp_details(result)
    # creates object to represent the specific passepartout for this graphic in the group
    window = create_gui(result)
    # create visual representation of results
