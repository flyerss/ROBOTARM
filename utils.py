
def generate_instruction(command, start_points=[], end_points=[]):
    # 传入的起始点可以是三元组，也可以是三元组数组
    def ensure_list(point):
        if isinstance(point, tuple):
            return [point]
        elif isinstance(point, list):
            return point
        else:
            raise ValueError("输入的起始点或终止点格式错误")

    start_list = ensure_list(start_points)
    end_list = ensure_list(end_points)

    instructions = []
    if command == 'reset':
        instructions.append('M0')
        return instructions
    elif command == 'move' and len(start_points) ==0 and len(end_points)==1: #不指定起始点默认向endpoints运动一次
        instructions.append(f'M4 X{end_points[0][0]} Y{end_points[0][1]} Z{end_points[0][2]}')
        return instructions
    elif command == 'move' and len(start_points) ==1 and len(end_points)==1: #起点到终点往复运动
        instructions.append(f'M4 X{start_points[0][0]} Y{start_points[0][1]} Z{start_points[0][2]}')
        instructions.append(f'M4 X{end_points[0][0]} Y{end_points[0][1]} Z{end_points[0][2]}')
        return instructions


