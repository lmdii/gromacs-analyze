import pymol

path = r"D:\Desktop\temp\ligand.gro"


def exalt_sele_resi(sele_name):
    res_list = pymol.cmd.get_model(sele_name).atom
    # 根据序列号进行排序
    res_list.sort(key=lambda x: x.resi_number)
    # 将残基序列号存储到列表中
    res_num_list = [r.resi_number for r in res_list]
    res_num_list = list(set(res_num_list))
    res_num_list.sort()
    return res_num_list


if __name__ == "__main__":
    # pymol.finish_launching()
    pymol.cmd.load(path, 'protein_RNA')
    pymol.cmd.select("RNA", "polymer.nucleic")
    pymol.cmd.select("connect_domain", "polymer.protein and resi 122-277")
    pymol.cmd.select("near_rna", "byres (rna around 4) and polymer.protein and resi 122-277")
    pymol.cmd.select("near_protein", "byres (connect_domain around 4) and polymer.nucleic")
    exalt_rna_resi = exalt_sele_resi("near_protein")
    exalt_domain_resi = exalt_sele_resi("near_rna")
