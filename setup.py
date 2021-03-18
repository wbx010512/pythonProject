import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(

    # 包的名称
    name="example_packg",

    # 版本号
    version="0.0.1",

    # 制作包的作者名称
    author="wbx",

    # pypi账户的邮箱
    author_email="wbx481742959@Outlook.com",

    # 包的简要描述
    description="a example package",

    # 长描述：一般写在README.md文件中
    long_description=long_description,

    # README.md文字标识，默认即可
    long_description_content_type="text/markdown",

    # 代码的存放地址(https://github.com/你的github账户名/github代码仓库名.git)
    # 代码仓库名就是项目名
    url="https://github.com/wbx010512/pythonProject.git",

    # 默认这样写即可，暂时不清楚作用
    packages=setuptools.find_packages(),

    # 项目依赖库
    install_requires=[''],

    # 项目依赖的python版本，操作系统，开源许可证等
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)