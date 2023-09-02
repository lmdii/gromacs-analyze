import pymol

protein_A_path = r"D:\Desktop\temp\ligand.gro"
protein_B_path = r"D:\Desktop\temp\protein3.gro"

#align A To sele B -> default:""
selectionA = 'protein_A and resi 225-275'
selectionB = 'protein_B and resi 225-275'


if __name__ == "__main__":

    # 创建pymol对象
    pymol.finish_launching()

    # 读入蛋白A和蛋白B的pdb文件
    pymol.cmd.load(protein_A_path, 'protein_A')
    pymol.cmd.load(protein_B_path, 'protein_B')

    pymol.cmd.select("seleA", selectionA)
    pymol.cmd.select("seleB", selectionB)

    pymol.cmd.color('smudge', 'protein_B')
    pymol.cmd.color("cyan", "seleA and ss h")
    pymol.cmd.color("magenta", "seleA and ss s")
    pymol.cmd.color("orange", "seleA and ss l")
    pymol.cmd.color("cyan", "seleB and ss h")
    pymol.cmd.color("magenta", "seleB and ss s")
    pymol.cmd.color("orange", "seleB and ss l")


    pymol.cmd.align('protein_A', selectionB, cycles=0)