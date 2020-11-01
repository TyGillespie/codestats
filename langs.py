import os

languages = []


class Language:
	def __init__(self, name, extensions, parent_lang="", associated_files=[]):
		self.name = name
		self.extensions = extensions
		self.associated_files = associated_files
		self.parent_lang = parent_lang
		languages.append(self)

	def __str__(self):
		final = self.name
		if self.parent_lang:
			final += " (" + self.parent_lang + ")"
		return final


# here we keep the data for all known languages
# todo: possibly integrate with a database (linguist) for more accurate results
# note: the following was mostly generated with a script. I've attempted to clean it up but might have missed something.

Language("AngelScript", [".as", ".angelscript"], "C++")
Language(
	"ApacheConf",
	[".apacheconf", ".vhost"],
	associated_files=[".htaccess", "apache2.conf", "httpd.conf"],
)
Language("Apollo Guidance Computer", [".agc"], "assembly_x86")
Language("AppleScript", [".scpt", ".applescript"])
Language("ASP", [".asp", ".aspx", ".asax", ".ascx", ".ashx", ".asmx", ".axd"])
Language("assembly", [".asm", ".a51", ".inc", ".nasm"])
Language("AutoHotkey", [".ahk", ".ahkl"])
Language("autoit", [".au3"])
Language("batchfile", [".bat", ".cmd"])
Language("BGT", [".bgt"])
Language("brainfuck", [".bf", ".b"])
Language("C/C++", [".c", ".cpp", ".c++", ".cc", ".cxx", ".h", ".hpp", ".h++", ".hxx"])
# thanks Ty
Language("C# (CSharp)", [".cs", ".csx", ".cake"])
# Language("chuck", (".ck"))
Language("CSS", [".css"])
Language("CSV", [".csv"])
Language("cython", [".pyx", ".pxd", ".pyi"])
Language("dockerfile", [".dockerfile"], associated_files=["dockerfile"])
Language("F#", [".fs", ".fsi", ".fsx"])
Language("go", [".go"])
Language("HTML", [".html", ".htm", ".html.hl", ".xht", ".xhtml"])
Language("HTML+Django", [".jinja", ".jinja2", ".mustache", ".njk"])
Language("HTML+ERB", [".erb", ".erb.deface"])
Language("HTML+PHP", [".phtml"])
Language("HTTP", [".http"])
Language(
	"INI",
	[".ini", ".cfg", ".lektorproject", ".prefs", ".pro", ".properties"],
	associated_files=[".editorconfig", ".gitconfig", "buildozer.spec"],
)
Language("Inno Setup", [".iss"])
Language("java", [".java"])
Language("java server pages", [".jsp"])
Language(
	"javascript",
	[
		".js",
		"._js",
		".bones",
		".es",
		".es6",
		".frag",
		".gs",
		".jake",
		".jscad",
		".jsfl",
		".jsm",
		".mjs",
		".njs",
		".pac",
		".sjs",
		".ssjs",
		".xsjs",
		".xsjslib",
	],
)
Language("jaws script", [".jsb", ".jss"])
Language("LOLCode", [".lol"])
Language("Linux Kernel Module", [".mod"])
Language("lua", [".lua", ".wlua"])
Language(
	"makefile",
	[".mak", ".make", ".mk", ".mkfile"],
	associated_files=[
		"BSDmakefile",
		"GNUmakefile",
		"Kbuild",
		"Makefile",
		"Makefile.am",
		"Makefile.boot",
		"Makefile.frag",
		"Makefile.in",
		"Makefile.inc",
		"Makefile.wat",
		"makefile",
		"makefile.sco",
		"mkfile",
	],
)
Language(
	"markdown",
	[
		".md",
		".markdown",
		".mdown",
		".mdwn",
		".mkd",
		".mkdn",
		".mkdown",
		".ronn",
		".workbook",
	],
	parent_lang="text",
)
Language("moo", [".moo"])
Language("Nmap Scripting Engine", [".nse"], parent_lang="lua")
Language("NSIS", [".nsi", ".nsh"])
Language("Nginx", [".nginxconf"], associated_files=["nginx.conf"])
Language("PHP", [".php", ".php3", ".php4", ".php5", ".phps", ".phpt"])
Language(
	"Perl",
	[".pl", ".al", ".perl", ".plx", ".pm"],
	associated_files=["Makefile.PL", "rexfile", "ack", "cpanfile"],
)
Language("Powershell", [".ps1", ".psd1", ".psm1"])
Language("PureBasic", [".pb", ".pbi"])
Language(
	"python",
	[".py", ".pyw", ".py2", ".py3", ".pyi", ".pip"],
	associated_files=[
		".gclient",
		"BUCK",
		"BUILD",
		"BUILD.bazel",
		"SConscript",
		"SConstruct",
		"Snakefile",
		"WORKSPACE",
		"wscript",
	],
)
Language("Regular Expression", [".regexp", ".regex"])
Language(
	"ruby",
	[
		".rb",
		".builder",
		".eye",
		".gemspec",
		".god",
		".jbuilder",
		".mspec",
		".pluginspec",
		".podspec",
		".rabl",
		".rake",
		".rbuild",
		".rbw",
		".rbx",
		".ruby",
		".thor",
		".watchr",
	],
	associated_files=[
		".irbrc",
		".pryrc",
		"Appraisals",
		"Berksfile",
		"Brewfile",
		"Buildfile",
		"Capfile",
		"Dangerfile",
		"Deliverfile",
		"Fastfile",
		"Gemfile",
		"Gemfile.lock",
		"Guardfile",
		"Jarfile",
		"Mavenfile",
		"Podfile",
		"Puppetfile",
		"Rakefile",
		"Snapfile",
		"Thorfile",
	],
)
Language("rust", [".rs", ".rs.in"])
Language(
	"shell script",
	[".sh", ".bash", ".ksh", ".sh.in", ".tmux", ".zsh"],
	associated_files=[
		".bash_logout",
		".bash_profile",
		".bashrc",
		".login",
		".profile",
		".zlogin",
		".zlogout",
		".zprofile",
		".zshenv",
		".zshrc",
	],
)
Language("swift", [".swift"])
Language(
	"visual basic", [".vb", ".bas", ".cls", ".frm", ".frx", ".vba", ".vbhtml", ".vbs"]
)
Language("windows registry entry", [".reg"])


def detect_lang(filename):
	file_ext = os.path.splitext(filename)[1]
	for i in languages:
		if file_ext in i.extensions:
			return i
		if filename in i.associated_files:
			return i
