USE [master]
GO
/****** Object:  Database [98point6_drop_token]    Script Date: 5/21/2020 10:40:46 PM ******/
CREATE DATABASE [98point6_drop_token]
 CONTAINMENT = NONE
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [98point6_drop_token].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [98point6_drop_token] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [98point6_drop_token] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [98point6_drop_token] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [98point6_drop_token] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [98point6_drop_token] SET ARITHABORT OFF 
GO
ALTER DATABASE [98point6_drop_token] SET AUTO_CLOSE ON 
GO
ALTER DATABASE [98point6_drop_token] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [98point6_drop_token] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [98point6_drop_token] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [98point6_drop_token] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [98point6_drop_token] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [98point6_drop_token] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [98point6_drop_token] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [98point6_drop_token] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [98point6_drop_token] SET  DISABLE_BROKER 
GO
ALTER DATABASE [98point6_drop_token] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [98point6_drop_token] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [98point6_drop_token] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [98point6_drop_token] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [98point6_drop_token] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [98point6_drop_token] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [98point6_drop_token] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [98point6_drop_token] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [98point6_drop_token] SET  MULTI_USER 
GO
ALTER DATABASE [98point6_drop_token] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [98point6_drop_token] SET DB_CHAINING OFF 
GO
ALTER DATABASE [98point6_drop_token] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [98point6_drop_token] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [98point6_drop_token] SET DELAYED_DURABILITY = DISABLED 
GO
USE [98point6_drop_token]
GO
/****** Object:  Table [dbo].[game_data]    Script Date: 5/21/2020 10:40:46 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[game_data](
	[game_id] [varchar](max) NOT NULL,
	[player_id] [varchar](max) NOT NULL,
	[move_number] [tinyint] NOT NULL,
	[column] [tinyint] NOT NULL,
	[result] [tinyint] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[game_results]    Script Date: 5/21/2020 10:40:46 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[game_results](
	[id] [tinyint] NOT NULL,
	[value] [varchar](50) NULL,
 CONSTRAINT [PK_game_results] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[player_addresses]    Script Date: 5/21/2020 10:40:46 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[player_addresses](
	[player_id] [int] NOT NULL,
	[street] [nvarchar](max) NULL,
	[city_id] [int] NULL,
	[state_id] [int] NULL,
	[postal_code] [varchar](50) NULL,
	[country_id] [int] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[player_cities]    Script Date: 5/21/2020 10:40:46 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[player_cities](
	[id] [int] NOT NULL,
	[value] [nvarchar](max) NULL,
 CONSTRAINT [PK_player_cities] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[player_countries]    Script Date: 5/21/2020 10:40:46 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[player_countries](
	[id] [int] NOT NULL,
	[value] [varchar](max) NULL,
 CONSTRAINT [PK_player_countries] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[player_genders]    Script Date: 5/21/2020 10:40:46 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[player_genders](
	[id] [int] NOT NULL,
	[value] [varchar](max) NULL,
 CONSTRAINT [PK_player_genders] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[player_images]    Script Date: 5/21/2020 10:40:46 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[player_images](
	[player_id] [int] NULL,
	[thumbnail] [varchar](max) NULL,
	[medium] [varchar](max) NULL,
	[large] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[player_logins]    Script Date: 5/21/2020 10:40:46 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[player_logins](
	[player_id] [int] NOT NULL,
	[username] [varchar](max) NULL,
	[salt] [varchar](max) NULL,
	[password_hashed] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[player_states]    Script Date: 5/21/2020 10:40:46 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[player_states](
	[id] [int] NOT NULL,
	[value] [nvarchar](max) NULL,
 CONSTRAINT [PK_player_states] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[player_titles]    Script Date: 5/21/2020 10:40:46 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[player_titles](
	[id] [int] NOT NULL,
	[value] [varchar](max) NULL,
 CONSTRAINT [PK_player_titles] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[players]    Script Date: 5/21/2020 10:40:46 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[players](
	[id] [int] NOT NULL,
	[title_id] [int] NULL,
	[name_first] [nvarchar](max) NULL,
	[name_last] [nvarchar](max) NULL,
	[email] [nvarchar](max) NULL,
	[date_of_birth] [date] NULL,
	[registration_time] [smalldatetime] NULL,
	[gender_id] [int] NULL,
	[phone_main] [varchar](50) NULL,
	[phone_cell] [varchar](50) NULL,
 CONSTRAINT [PK_players] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[game_data]  WITH CHECK ADD  CONSTRAINT [FK_game_data_game_results] FOREIGN KEY([result])
REFERENCES [dbo].[game_results] ([id])
GO
ALTER TABLE [dbo].[game_data] CHECK CONSTRAINT [FK_game_data_game_results]
GO
ALTER TABLE [dbo].[player_addresses]  WITH CHECK ADD  CONSTRAINT [FK_player_addresses_player_cities] FOREIGN KEY([city_id])
REFERENCES [dbo].[player_cities] ([id])
GO
ALTER TABLE [dbo].[player_addresses] CHECK CONSTRAINT [FK_player_addresses_player_cities]
GO
ALTER TABLE [dbo].[player_addresses]  WITH CHECK ADD  CONSTRAINT [FK_player_addresses_player_countries] FOREIGN KEY([country_id])
REFERENCES [dbo].[player_countries] ([id])
GO
ALTER TABLE [dbo].[player_addresses] CHECK CONSTRAINT [FK_player_addresses_player_countries]
GO
ALTER TABLE [dbo].[player_addresses]  WITH CHECK ADD  CONSTRAINT [FK_player_addresses_player_states] FOREIGN KEY([state_id])
REFERENCES [dbo].[player_states] ([id])
GO
ALTER TABLE [dbo].[player_addresses] CHECK CONSTRAINT [FK_player_addresses_player_states]
GO
ALTER TABLE [dbo].[player_addresses]  WITH CHECK ADD  CONSTRAINT [FK_player_addresses_players] FOREIGN KEY([player_id])
REFERENCES [dbo].[players] ([id])
GO
ALTER TABLE [dbo].[player_addresses] CHECK CONSTRAINT [FK_player_addresses_players]
GO
ALTER TABLE [dbo].[player_images]  WITH CHECK ADD  CONSTRAINT [FK_player_images_players] FOREIGN KEY([player_id])
REFERENCES [dbo].[players] ([id])
GO
ALTER TABLE [dbo].[player_images] CHECK CONSTRAINT [FK_player_images_players]
GO
ALTER TABLE [dbo].[player_logins]  WITH CHECK ADD  CONSTRAINT [FK_player_logins_players] FOREIGN KEY([player_id])
REFERENCES [dbo].[players] ([id])
GO
ALTER TABLE [dbo].[player_logins] CHECK CONSTRAINT [FK_player_logins_players]
GO
ALTER TABLE [dbo].[players]  WITH CHECK ADD  CONSTRAINT [FK_players_player_genders] FOREIGN KEY([gender_id])
REFERENCES [dbo].[player_genders] ([id])
GO
ALTER TABLE [dbo].[players] CHECK CONSTRAINT [FK_players_player_genders]
GO
ALTER TABLE [dbo].[players]  WITH CHECK ADD  CONSTRAINT [FK_players_player_titles] FOREIGN KEY([title_id])
REFERENCES [dbo].[player_titles] ([id])
GO
ALTER TABLE [dbo].[players] CHECK CONSTRAINT [FK_players_player_titles]
GO
USE [master]
GO
ALTER DATABASE [98point6_drop_token] SET  READ_WRITE 
GO
